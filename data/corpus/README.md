# PRBEN Corpus

This dataset contains document shards for BM25 / RAG retrieval.

## Format

Each line is a JSON object:

{"id": "...", "contents": "..."}

## Usage

```python
from datasets import load_dataset
dataset = load_dataset("prben-ai/PRBEN")
