## `D_star.jsonl`

Maps each anonymized ID to its golden relevant documents.

### Example

```json
{
  "id": "prben_id_00001",
  "docs_list": ["doc1","doc2"]
}
```

### Fields

| Field | Description |
|---|---|
| `id` | Anonymized sample ID |
| `value` | List of golden relevant documents |

---

## `Y_star.jsonl`

Contains extracted keywords and generated reference answers.

### Example

```json
{
  "id": "prben_id_00001",
  "value": {
    "key_words": [
      "sleep",
      "health",
      "insomnia"
    ],
    "answer": "Improving sleep quality usually involves..."
  }
}
```

### Fields

| Field | Description |
|---|---|
| `id` | Anonymized sample ID |
| `key_words` | Extracted intent keywords |
| `answer` | Reference answer |
