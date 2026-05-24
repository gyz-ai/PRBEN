# Document Corpus

This folder contains document shards for BM25 indexing.

## Format

Each line is a JSON object:

{"id": "...", "contents": "..."}

## Usage

Run:

bash scripts/build_bm25_index.sh
