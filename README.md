# PRBEN
Personalized RAG in the Wild: Benchmarking Personalized RAG with Authentic User Behavioral Signals
## Introduction
We introduce PRBEN, a new benchmark based on the popular Chinese search engine Baidu.com. PRBEN includes 800 users, whose historical queries, click logs, and profile information were collected over a three-month period from July 1 to September 30, 2025. In this dataset, we record users’ real queries and all clicked URLs along with their associated attributes, covering diverse topics and query types. Using our construction method, we generated a gold-standard reference that reflects users’ personalized needs, providing an evaluable benchmark for research on personalized retrieval and generation methods.
<p align="center">
<img src="https://github.com/user-attachments/assets/00dddcdc-f388-4455-90ac-d170e3932e31" width="600" height="320" />
</p>

The dataset is derived from anonymized search logs. To protect user privacy, we applied 𝑘-anonymity filtering (k=5) and masked all personally identifiable information (PII) using named entity recognition (NER). The dataset is released under a strict research-only license, and any attempts to re-identify users are strictly prohibited.

## Dataset Statistics
The basic statistics of PRBEN dataset shows as follow:
| Statistic                     | Value                     |
|--------------------------------|---------------------------|
| Sample size                    | 800                       |
| History query length (range)   | 2–493                     |
| History query length (average) | 194                       |
| Gender distribution            | Female: 49.11%; Male: 50.89% |
| Age range                      | 0–65+                     |
| Number of provinces            | 31                        |


## Data Content and Format
The dataset is provided in .tar.gz format and can be decompressed using the following command:
After decompression, the folder PRBEN will contain two files: user_data.jsonl and data_gold_target.jsonl.

### (1)user_data.jsonl
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
  
### (2)data_gold_target.jsonl

This file contains the gold document set for the retrieval stage and the gold answers with corresponding keywords for the generation stage.  
The format of each line of data in this file is：
```json
{"user_id": ,"gold_docs": ,"gold_answer": ,"gold_keywords":  }
```
- user_id: the anonymized PRBEN ID of the user.
- gold_docs: the set of gold documents for the retrieval stage.  
- gold_answer: the gold answer for the generation stage.  
- gold_keywords: the keywords associated with the gold answer.

## Corpus
This corpus contains 2,341,338 base documents, all sourced from real online Baidu links. The documents are stored in the following format:
```json
{"id": ,"contents": }
```
- id: the ID of the document in the text corpus.
- contents: the textual content of the document.
  
The corpus can be downloaded from the following Hugging Face URL:

## Baseline models
We evaluated several open-source and closed-source models on our benchmark.
The following presents a subset of our results：

| Method(Personalized Retrieval) | Recall | MRR    | NDCG   | MAP    | Relevance |
|--------------------------------|--------|--------|--------|--------|-----------|
| **Long History ** |        |        |        |        |           |
| Gemini-1.5-Pro                  | 0.2430 | 0.4538 | 0.2685 | 0.1776 | 0.2005    |
| DeepSeek-R1                     | 0.2200 | 0.4046 | 0.2424 | 0.1645 | 0.1756    |
| Qwen-2.5-7B-Instruct-SFT        | 0.2279 | 0.4226 | 0.2506 | 0.1677 | 0.1770    |
| **Short History** |        |        |        |        |           |
| Gemini-1.5-Pro                  | 0.2769 | 0.5153 | 0.3076 | 0.2092 | 0.2129    |
| DeepSeek-R1                     | 0.2664 | 0.4807 | 0.2924 | 0.2008 | 0.2041    |
| Qwen-2.5-7B-Instruct-SFT        | 0.2884 | 0.5066 | 0.3163 | 0.2200 | 0.1901    |
| **Long + Short History** |        |        |        |        |           |
| Gemini-1.5-Pro                  | 0.2780 | 0.5111 | 0.3081 | 0.2106 | 0.2148    |
| DeepSeek-R1                     | 0.2846 | 0.5085 | 0.3143 | 0.2179 | 0.1964    |
| Qwen-2.5-7B-Instruct-SFT        | 0.2897 | 0.5159 | 0.3190 | 0.2219 | 0.2009    |

Additionally, we evaluated the models’ performance on the complete end-to-end pipeline.
The following presents a subset of our results：

| Method | BLEU    | ROUGE-L  | PGDC     | PTC      | Faithfulness | Factuality |
|--------|---------|----------|----------|----------|--------------|------------|
| dp (P-P)     | 0.0622 | 0.2064 | 0.8018 | 0.4361 | 0.6094 | 0.7304 |
| qw (P-P)     | 0.0549 | 0.1883 | 0.5601 | 0.2997 | 0.6697 | 0.5672 |
| gemini (P-P) | 0.1315 | 0.2686 | 0.7556 | 0.5697 | 0.6123 | 0.8060 |

<img width="700" height="250" alt="3151770979516_ pic" src="https://github.com/user-attachments/assets/e6ebb75e-ae4f-4c33-9806-bedf88685d6c" />


  
### License
This repository is liciensed under Apache-2.0 License.

The PRBEN benchmark is liciensed under CC BY-NC-SA 4.0.

## FQA

