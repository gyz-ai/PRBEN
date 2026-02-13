# PRBEN
Personalized RAG in the Wild: Benchmarking Personalized RAG with Authentic User Behavioral Signals
# Introduction
# Dataset Statistics
The basic statistics of PRBEN dataset shows as follow:

# Data Content and Format
## user_data.jsonl

This file contains the user information, user_id, query, click_url, history_querys, gender, age, province.The format of each line of data in this file is：

## data_gold_target.jsonl

This file contains the gold document set for the retrieval stage and the gold answers with corresponding keywords for the generation stage.  
Each line in this file follows the format:
