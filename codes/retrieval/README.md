## Retrieval

Run BM25 retrieval using Pyserini:

```bash
python retrieval/search_queries.py \
  --index_dir data/indexes/docs_idx \
  --input_dir data/queries/rewrite_gemini \
  --output_dir data/retrieval_results/rewrite_gemini \
  --topk 10
```

