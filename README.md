# PRBEN
Personalized RAG in the Wild: Benchmarking Personalized RAG with Authentic User Behavioral Signals
# Introduction
# Dataset Statistics
The basic statistics of PRBEN dataset shows as follow:

# Data Content and Format
## user_data.jsonl
This file contains the user information, user_id, query, click_url, long_history_querys, gender, age, province.The format of each line of data in this file is：
{ "user_id": 
  "prben_id_0005", 
  "query": "甲骨文", 
  "click_url": ["http://www.oracle.com/index.html"], 
  "long_history_query": ["甲骨文", "宁晋县雄达机械有限公司", "火影忍者720集全集免费版", "火影忍者", "寻秦记 2018 陈翔", "《寻秦记》电视剧", "《寻秦记》电视剧", "哈啰", "滴滴24人工投诉电话", "滴滴快送怎么转人工", "滴滴24小时人工客服电话", "滴滴司机人工客服", "滴滴出行客服", "滴滴出行顺风车客服24小时人工电话", "滴滴出行顺风车", "生万物", "48国标螺母牙距是多少", "东八里庄小区距离天安门多远", "天龙八部主题曲", "天龙八部手游荣耀版", "黄金荣和杜月笙谁更厉害", "黄金荣", "石家庄到北京高铁", "男人梦见拉裤裆屎财运", "做梦梦到拉屎拉裤子里了", "寻秦记国语在线观看免费完整版", "《寻秦记》电视剧", "寻秦记国语在线观看免费完整版", "《寻秦记》电视剧", "《寻秦记》电视剧", "寻秦记电视剧", "寻秦记电影", "寻秦记", "寻秦记", "寻秦记", "五台山天气预报", "石家庄天气", "浪浪山小妖怪在线观看免费高清电视剧大全", "浪浪山小妖怪在线观看免费高清电视剧大全", "浪浪山小妖怪全集免费看", "浪浪山的小妖怪在线观看", "浪浪在线观看免费高清电视剧大全", "浪浪山的小妖怪在线观看", "浪浪山的小妖怪在线观看", "浪浪山的小妖怪在线观看", "浪浪山的小妖怪", "安源是谁出租车", "安源是谁", "上海秦奋的爷爷是谁", "秦奋", "京津冀等9省区市部分地区将迎暴雨", "帝师是什么身份背景", "稳定币美股circle", "白兆雄", "白兆雄 马拉松", "白兆雄", "科技巨头Palantir", "palantir", "谷歌AI公司有哪些", "palantir", "稳定币美股circle", "稳定币美股circle", "稳定币和比特币的区别", "稳定币和数字货币的区别", "稳定币", "稳定币美股circle", "稳定币美股circle", "蓝翠竹", "蓝翠竹", "蓝翠竹", "蓝翠竹亮证姐", "蓝翠珠", "兰翠珠", "兰翠珠防城港", "兰翠思", "显卡排行", "七彩虹", "七彩虹", "英伟达", "全球利润最高的公司", "meta", "稳定币美股circle", "北京天气", "稳定币美股circle", "稳定币美股circle", "稳定币美股circle", "稳定币三张牌照给了谁", "香港稳定币条例生效在即", "香港稳定币牌照哪几家", "稳定币美股circle", "稳定币美股circle", "稳定币美股价格走势", "稳定币美股circle", "稳定币美股circle", "寻亲寻人网官网", "稳定币美股circle", "稳定币美股circle", "稳定币美股circle", "稳定币美股走势", "稳定币美股", "稳定币最新消息", "Circle股价", "Circle股价", "Circle股价", "Circle股价", "美国稳定币股票", "美国稳定币", "天山水泥西藏有分公司吗", "极狐阿尔法s5", "buildmost", "build", "金山云", "勾魂恶梦", "http://725g.cc/", "黄仁勋", "勾魂恶梦", "勾魂恶梦", "勾魂恶梦", "core scientific", "王者荣耀一年利润", "王者荣耀一年收入多少钱", "劳斯莱斯为啥叫库里南", "库里南", "宁晋县中考录取分数线2025", "宁晋县中考录取分数线2025", "宁晋县中考录取分数线2025", "03195517702", "河北工业大学", "宁晋县小升初总分是多少", "宁晋县小升初总分是多少", "宁晋县到青岛多少公里", "青岛天气", "青岛天气", "小米", "河北600分以上人数", "河北600分能上什么大学"], 
  "gender": "男", 
  "age": "35-44", 
  "province": "河北省"}

## data_gold_target.jsonl

This file contains the gold document set for the retrieval stage and the gold answers with corresponding keywords for the generation stage.  
The format of each line of data in this file is：
