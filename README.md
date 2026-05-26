# PRBEN
Personalized RAG in the Wild: Benchmarking Personalized RAG with Authentic User Behavioral Signals
## Introduction
We introduce PRBEN, a new benchmark based on the popular Chinese search engine. PRBEN includes 10408 users, whose historical queries, click logs, and profile information were collected over a three-month period. In this dataset, we record users’ real queries and all clicked URLs along with their associated attributes, covering diverse topics and query types. Using our construction method, we generated a gold-standard reference that reflects users’ personalized needs, providing an evaluable benchmark for research on personalized retrieval and generation methods.
<!-- <p align="center">
<img src="https://github.com/user-attachments/assets/3619af74-d323-46da-ad7b-60a0953d1c56" width="600" height="320" />
</p> -->
<!-- <p align="center">
<img src="https://github.com/user-attachments/assets/3619af74-d323-46da-ad7b-60a0953d1c56" width="600" height="320" />
</p> -->
<!-- <p align="center">
<img width="800" height="400" alt="PRBEN" src="https://github.com/user-attachments/assets/312d7c10-32b0-4f99-acec-5211bac7196b" />
</p> -->
<img width="2226" height="1013" alt="PRBEN" src="https://github.com/user-attachments/assets/a85549d5-157d-4807-a57a-040cc0125a5f" />

The dataset is derived from anonymized search logs. To protect user privacy, we applied 𝑘-anonymity filtering (k=5) and masked all personally identifiable information (PII) using named entity recognition (NER). The dataset is released under a strict research-only license, and any attempts to re-identify users are strictly prohibited.

## Dataset Statistics
The basic statistics of PRBEN dataset shows as follow:
| Statistic                     | Value                     |
|--------------------------------|---------------------------|
| Sample size                    | 10408                      |
| History query length (range)   | 2–823                    |
| History query length (average) | 211                      |
| Gender distribution            | Female: 54.80%; Male: 45.20% |
| Age range                      | 0–65+                     |
| Number of provinces/regions      | 32                        |

## Project Structure

The PRBEN repository is organized into four major components: retrieval, generation, evaluation, and datasets.  
The `codes/` directory contains the core personalized retrieval and answer generation pipelines.  
The `data/` directory stores retrieval corpora, user behavior data, gold annotations, and retrieval outputs.  
The `evaluation/` directory provides both retrieval and generation evaluation scripts, including lexical overlap metrics, personalization consistency metrics, factuality evaluation, and faithfulness scoring.  
Utility scripts such as BM25 index construction are placed under `scripts/`.  
Detailed descriptions, data formats, and usage instructions are provided in the README files inside each subdirectory, allowing users to quickly set up the project and start retrieval and generation evaluation.

```text
PRBEN/
├── codes/
│   ├── retrieval/
│   │   ├── bm25_retriever.py
│   │   └── retrieval_prompt.py
│   │
│   └── generation/
│       └── generation_prompt.py
│
├── scripts/
│   └── build_bm25_index.sh
│
├── data/
│   ├── corpus/
│   │   ├── download.sh
│   │   └── manifest.json
│   │
│   ├── gold/
│   │   ├── D_star.jsonl
│   │   └── Y_star.jsonl
│   │
│   ├── user_data/
│   │   ├── user_click_url.jsonl
│   │   ├── user_history_part1.jsonl
│   │   ├── user_history_part2.jsonl
│   │   ├── user_history_part3.jsonl
│   │   ├── user_profile.jsonl
│   │   └── user_query.jsonl
│   │
│   └── retrieval_results/
│
├── evaluation/
│   ├── retrieval/
│   │   └── retrieval_val.py
│   │
│   └── generation/
│       ├── BLEU.py
│       ├── PGDC.py
│       ├── PTC.py
│       ├── ROUGEL.py
│       ├── factuality.py
│       └── faithfulness.py
│
├── requirements.txt
└── README.md
```
<!--
## Data Content and Format
The folder PRBEN will contain three files: user_data.jsonl , data_gold_target.jsonl and prompt.py.

### (1) user_data.jsonl
This file contains the user information, user_id, query, click_url, long_history_querys, gender, age, province.The format of each line of data in this file is：

```json
{"user_id": ,"query": ,"click_url": ,"long_history_query": ,"gender": ,"age": ,"province": }
```
- user_id: the anonymized PRBEN ID of the user.
- query: the user’s current query.
- click_url: the URLs clicked by the user for the current query.
- long_history_query: the user’s long-term historical queries.
- gender: the user’s gender.  
- age: the user’s age range.  
- province: the user’s location (province).
  
### (2) data_gold_target.jsonl

This file contains the gold document set for the retrieval stage and the gold answers with corresponding keywords for the generation stage.  
The format of each line of data in this file is：
```json
{"user_id": ,"gold_docs": ,"gold_answer": ,"gold_keywords":  }
```
- user_id: the anonymized PRBEN ID of the user.
- gold_docs: the set of gold documents for the retrieval stage.  
- gold_answer: the gold answer for the generation stage.  
- gold_keywords: the keywords associated with the gold answer.
  
### (3) prompt.py
The prompt.py file encapsulates the key prompts employed in both the personalized retrieval and personalized generation stages. These prompts are crucial for guiding the model to:
- Personalized Retrieval – adapt the search process based on the user’s historical interactions and preferences.
- Personalized Generation – generate responses that are aligned with the user’s intent and personalized context.
  
## Corpus
This corpus contains 2,341,338 base documents, all sourced from real online Baidu links. The documents are stored in the following format:
```json
{"id": ,"contents": }
```
- id: the ID of the document in the text corpus.
- contents: the textual content of the document.
  
The corpus can be downloaded from the following Hugging Face URL:https://huggingface.co/datasets/gyz-ai/PRBEN
-->

## Baseline models
We evaluate several open-source and closed-source models on our benchmark. 
The following presents a subset of the results at @10.

| Personalized Retrieval | Recall@10 | MRR@10 | NDCG@10 | MAP | Relevance |
|--------------------------------|-----------|--------|---------|------|-----------|
| **Non-Personalized Retrieval** |
| BM25                          | 0.1902 | 0.3746 | 0.2070 | 0.1218 | 0.0519 |
| Q2D                           | 0.0459 | 0.1273 | 0.0514 | 0.0220 | 0.0796 |
| BART                          | 0.1837 | 0.3619 | 0.1997 | 0.1171 | 0.0390 |
| Gemini-2.5                    | 0.1541 | 0.3129 | 0.1691 | 0.0997 | 0.0833 |
| DeepSeek-R1                   | 0.1726 | 0.3499 | 0.1901 | 0.1123 | 0.0727 |
| Qwen-2.5-7B-Instruct         | 0.1547 | 0.3220 | 0.1702 | 0.0980 | 0.0281 |
| **Long History** |
| Gemini-2.5                    | 0.2455 | 0.4493 | 0.2695 | 0.1807 | 0.0902 |
| DeepSeek-R1                   | 0.2440 | 0.4440 | 0.2671 | 0.1788 | 0.0665 |
| Qwen-2.5-7B-Instruct-SFT     | 0.2472 | 0.4508 | 0.2717 | 0.1843 | 0.0857 |
| **Short History** |
| Gemini-2.5                    | 0.2708 | 0.4827 | 0.2964 | 0.2032 | 0.0827 |
| DeepSeek-R1                   | 0.2638 | 0.4673 | 0.2883 | 0.1986 | 0.0597 |
| Qwen-2.5-7B-Instruct-SFT     | 0.2747 | 0.4889 | 0.3023 | 0.2117 | 0.0778 |
| **Long + Short History** |
| Gemini-2.5                    | 0.2859 | 0.5037 | 0.3130 | 0.2175 | 0.0867 |
| DeepSeek-R1                   | 0.2857 | 0.4979 | 0.3125 | 0.2191 | 0.0585 |
| Qwen-2.5-7B-Instruct-SFT     | 0.2972 | 0.5227 | 0.3272 | 0.2317 | 0.0828 |
| **User Attributes** |
| Gemini-2.5                    | 0.2032 | 0.3929 | 0.2236 | 0.1416 | 0.0845 |
| DeepSeek-R1                   | 0.1820 | 0.3541 | 0.1998 | 0.1239 | 0.0529 |
| Qwen-2.5-7B-Instruct-SFT     | 0.1905 | 0.3697 | 0.2099 | 0.1322 | 0.0815 |

Additionally, we evaluated the models’ performance on the complete end-to-end pipeline.
The following presents a subset of our results：

| Method | BLEU    | ROUGE-L  | PGDC     | PTC      | Faithfulness | Factuality |
|--------|---------|----------|----------|----------|--------------|------------|
|DeepSeek-R1(P-P)     | 0.0622 | 0.2064 | 0.8018 | 0.4361 | 0.6094 | 0.7304 |
| Qwen-2.5-7B-Instruct(P-P)     | 0.0549 | 0.1883 | 0.5601 | 0.2997 | 0.6697 | 0.5672 |
| Gemini-2.5(P-P) | 0.1315 | 0.2686 | 0.7556 | 0.5697 | 0.6123 | 0.8060 |

---

<img width="1209" height="312" alt="bar-simple" src="https://github.com/user-attachments/assets/720b9ee7-8969-4ef0-9c38-ee616708bab6" />

### License
This repository is liciensed under Apache-2.0 License.

The PRBEN benchmark is liciensed under CC BY-NC-SA 4.0.

## FQA

