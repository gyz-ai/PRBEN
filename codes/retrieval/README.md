## Retrieval

Run BM25 retrieval using Pyserini:

```bash
python retrieval/search_queries.py \
  --index_dir data/indexes/docs_idx \
  --input_dir data/queries/rewrite_gemini \
  --output_dir data/retrieval_results/rewrite_gemini \
  --topk 10
```

---

### Input Query Format

Input query files are stored in `.jsonl` format.

Example:

```json
{"id": "1001", "query": "适合女生的机械键盘推荐"}
{"id": "1002", "query": "东京旅游攻略"}
```

Fields:

- `id`: Query identifier
- `query`: Query text

---

### Retrieval Output Format

Retrieval outputs are stored in `.json` format.

Example:

```json
[
  {
    "query": "1001",
    "1": "doc_182||12.73",
    "2": "doc_991||11.42",
    "3": "doc_204||10.88"
  },
  {
    "query": "1002",
    "1": "doc_773||13.92",
    "2": "doc_511||12.44"
  }
]
```

Fields:

- `query`: Query identifier
- `1`, `2`, ... : Retrieved document rank
- `doc_id||score`: Retrieved document id and BM25 score

---

### Corpus Format

The document corpus is stored in `.jsonl` format.

Example:

```json
{
  "id": "doc_182",
  "contents": "机械键盘通常分为红轴、茶轴和青轴..."
}
```

Fields:

- `id`: Document identifier
- `contents`: Document text
