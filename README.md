# PRBEN
Personalized RAG in the Wild: Benchmarking Personalized RAG with Authentic User Behavioral Signals
# Introduction
# Dataset Statistics
The basic statistics of PRBEN dataset shows as follow:

# Data Content and Format
## user_data.jsonl
This file contains the user information, user_id, query, click_url, long_history_querys, gender, age, province.The format of each line of data in this file is：

```json
{
  "user_id": "prben_id_0005",
  "query": "甲骨文",
  "click_url": [
    "http://www.oracle.com/index.html"
  ],
  "long_history_query": [
    "甲骨文",
    "宁晋县雄达机械有限公司",
    "火影忍者720集全集免费版",
    "火影忍者",
    "寻秦记 2018 陈翔",
    "《寻秦记》电视剧",
    "...(省略若干条历史查询)..."
  ],
  "gender": "男",
  "age": "35-44",
  "province": "河北省"
}

## data_gold_target.jsonl

This file contains the gold document set for the retrieval stage and the gold answers with corresponding keywords for the generation stage.  
The format of each line of data in this file is：
