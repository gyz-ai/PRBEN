## Factuality Evaluation

Run factual correctness prompt generation:

```bash
python evaluation/build_fact_prompts.py \
  --input_dir data/answers \
  --output_dir data/fact_prompts
```

### Input Answer Format

Input answers are stored in `.jsonl` format.

Example:

```json
{"id": "prben_id_00001", "answer": "Paris is the capital of France."}
{"id": "prben_id_00002", "answer": "The Earth revolves around the Sun."}
```

Fields:

- `id`: Sample identifier
- `answer`: Generated answer to be evaluated

---

### Output Prompt Format

Generated factuality prompts are stored in `.jsonl` format.

Example:

```json
{
  "system": "",
  "src": [
    "你是一名严格的事实核查专家（Automated Fact Checker）..."
  ]
}
```

Fields:

- `system`: System prompt
- `src`: Prompt list for factual correctness evaluation

---

### Factual Correctness Scoring

The evaluator model outputs a continuous score between `0.0` and `1.0`.

Example:

```json
{"factual_correctness": 0.92}
```

Score interpretation:

- `1.0`: Highly factual and reliable
- `0.0`: Severely incorrect or hallucinated

---


## PGDC Evaluation

Run PGDC prompt generation:

```bash
python evaluation/build_pgdc_prompts.py \
  --gold_file data/gold/gold_answers.jsonl \
  --input_dir data/answers \
  --output_dir data/pgdc_prompts
```

### Gold Answer Format

Gold personalized answers are stored in `.jsonl` format.

Example:

```json
{"id": "prben_id_00001", "answer": "Personalized gold answer."}
{"id": "prben_id_00002", "answer": "Another personalized gold answer."}
```

Fields:

- `id`: Sample identifier
- `answer`: Personalized reference answer

---

### Generated Answer Format

Generated answers are stored in `.jsonl` format.

Example:

```json
{"id": "prben_id_00001", "answer": "Model generated answer."}
{"id": "prben_id_00002", "answer": "Another generated answer."}
```

Fields:

- `id`: Sample identifier
- `answer`: Model generated answer

---

### Output Prompt Format

Generated PGDC prompts are stored in `.jsonl` format.

Example:

```json
{
  "system": "",
  "src": [
    "你是一名个性化文本生成评测专家..."
  ]
}
```

Fields:

- `system`: System prompt
- `src`: Prompt list for PGDC evaluation

---

### PGDC Scoring

The evaluator model outputs an integer score between `1` and `5`.

Example:

```json
{"PGDC_score": 5}
```

Score interpretation:

- `5`: Highly consistent with personalized generation direction
- `1`: Completely inconsistent with personalized intent and preference

---
