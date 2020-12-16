from db.db_query import news_query
import requests

data=news_query()
title_list=[x['title'] for x in data]
seed=1
while seed:
    seed_text=''
    for title in title_list:
        seed_text=seed_text+title
        if len(seed_text)>10000:
            continue
        else:
            print(seed_text)
            pass
    seed=False

api_url='http://aiopen.etri.re.kr:8000/WiseNLU'
api_key='c1ec92a4-7b57-4262-9908-4e0e6d0e70dc'