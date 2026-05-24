#!/bin/bash

set -e

echo "========================================"
echo "Downloading PRBEN corpus from HuggingFace..."
echo "========================================"

mkdir -p data/docs/doc_files

# shard 0
wget -O data/docs/doc_files/shard_000.jsonl \
https://huggingface.co/datasets/prben-ai/PRBEN/blob/main/docs_000.jsonl

# shard 1
wget -O data/docs/doc_files/shard_001.jsonl \
https://huggingface.co/datasets/prben-ai/PRBEN/blob/main/docs_001.jsonl

echo "========================================"
echo "Download completed."
echo "========================================"
