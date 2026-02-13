# PRBEN
Personalized RAG in the Wild: Benchmarking Personalized RAG with Authentic User Behavioral Signals
## Introduction
We introduce PRBEN, a new benchmark based on the popular Chinese search engine Baidu.com. PRBEN includes 800 users, whose historical queries, click logs, and profile information were collected over a three-month period from July 1 to September 30, 2025. In this dataset, we record users’ real queries and all clicked URLs along with their associated attributes, covering diverse topics and query types. Using our construction method, we generated a gold-standard reference that reflects users’ personalized needs, providing an evaluable benchmark for research on personalized retrieval and generation methods.

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
  
### License
This repository is liciensed under Apache-2.0 License.

The PRBEN benchmark is liciensed under CC BY-NC-SA 4.0.

## FQA

