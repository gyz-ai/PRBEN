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


---



# Personalized Query Rewrite Prompt Construction This module constructs personalized query rewrite prompts for large language models (e.g., GPT-4.1, Qwen, Claude). The prompts are generated based on: - User recent search history - User long-term search interests - User profile attributes The framework is highly extensible. Different personalized features can be easily enabled or disabled by modifying the corresponding code sections. The top-5 historical records can be obtained using your own retrieval strategy or semantic similarity methods, and the generated prompts can then be applied to any target large language model for evaluation. ---

# Input Format

Each line in the input file should be a JSON object:

```json
{
  "id": "1",
  "query": "小米",
  "long_history": [
    "大众汽车",
    "特斯拉Model Y",
    "新能源汽车"
  ],
  "top_5_long_history": [
    "比亚迪汉",
    "蔚来ES6"
  ],
  "province": "北京",
  "age": "25",
  "gender": "男"
}
```

---

# Build Personalized Rewrite Prompts

Run:

```bash
python scripts/build_rewrite_prompt.py \
  --input_file data/queries/test.jsonl \
  --output_file data/prompts/rewrite_prompt.jsonl \
  --id_prompt_output_file data/prompts/id_prompt_mapping.jsonl
```

---

# Output Files

## Prompt File

```json
{
  "system": "",
  "src": [
    "prompt text ..."
  ]
}
```

## ID-Prompt Mapping File

```json
{
  "id": "1",
  "prompt": "prompt text ..."
}
```

---

# Feature Ablation

You can easily enable or disable different personalized features by modifying the corresponding code sections, including:
- Recent search history
- Long-term interests
- User profile information

This design supports flexible ablation experiments for personalized retrieval and personalized query rewriting research.

---
