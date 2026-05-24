import os
import json
import jieba
import argparse

from glob import glob
from tqdm import tqdm
from pyserini.search.lucene import LuceneSearcher


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--index_dir",
        type=str,
        required=True,
        help="Path to Lucene index"
    )

    parser.add_argument(
        "--input_dir",
        type=str,
        required=True,
        help="Directory containing query jsonl files"
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Directory to save retrieval results"
    )

    parser.add_argument(
        "--topk",
        type=int,
        default=10,
        help="Top-k retrieval results"
    )

    return parser.parse_args()


def main():

    args = parse_args()

    # =========================
    # Initialize Searcher
    # =========================
    searcher = LuceneSearcher(args.index_dir)

    # =========================
    # Create output directory
    # =========================
    os.makedirs(args.output_dir, exist_ok=True)

    # =========================
    # Load all jsonl files
    # =========================
    input_files = glob(os.path.join(args.input_dir, "*.jsonl"))

    print(f"Found {len(input_files)} files")

    # =========================
    # Process each file
    # =========================
    for input_file in input_files:

        print(f"\nProcessing: {input_file}")

        retrieval_results = []

        file_name = os.path.basename(input_file)

        output_file = os.path.join(
            args.output_dir,
            file_name
        )

        # =========================
        # Read jsonl
        # =========================
        with open(input_file, "r", encoding="utf-8") as f:

            for line in tqdm(f):

                if not line.strip():
                    continue

                try:
                    item = json.loads(line.strip())

                    query_id = str(item.get("id", "")).strip()

                    query = item.get("query", "").strip()

                    if not query:
                        continue

                    result_item = {}

                    result_item["query"] = query_id

                    # Chinese word segmentation
                    segmented_query = " ".join(
                        jieba.cut(query)
                    )

                    # Retrieval
                    hits = searcher.search(
                        segmented_query,
                        k=args.topk
                    )

                    # Save retrieval results
                    for rank, hit in enumerate(hits, start=1):

                        result_item[str(rank)] = (
                            f"{hit.docid}||{hit.score}"
                        )

                    retrieval_results.append(result_item)

                except Exception as e:
                    print(f"ERROR: {e}")

        # =========================
        # Save output
        # =========================
        with open(output_file, "w", encoding="utf-8") as fw:

            json.dump(
                retrieval_results,
                fw,
                ensure_ascii=False,
                indent=2
            )

        print(f"Saved to: {output_file}")
        print(f"Total queries: {len(retrieval_results)}")

    print("\nDone")


if __name__ == "__main__":
    main()
