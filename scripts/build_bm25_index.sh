#!/bin/bash

set -e

INPUT=data/docs/doc_files
OUTPUT=data/index/bm25

python -m pyserini.index.lucene \
  --collection JsonCollection \
  --input $INPUT \
  --index $OUTPUT \
  --generator DefaultLuceneDocumentGenerator \
  --storePositions \
  --storeDocvectors \
  --storeRaw
