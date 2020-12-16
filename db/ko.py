from db_query import news_query
import requests
from tqdm import tqdm
import json
import matplotlib.pyplot as plt
data=news_query()
title_list=[x['title'] for x in data]
seed=1
chunk_list=[]
while seed:
    if title_list:
        seed_text=''
        for title in tqdm(title_list):
            seed_text=seed_text+title
            if len(seed_text)>10000:
                print('for문 탈출')
                seed_text=seed_text[:-len(title)]
                chunk_list.append(seed_text)
                break
            else:
                title_list=title_list[1:]
                continue
    else:
        seed=False
print(len(chunk_list))


api_url='http://aiopen.etri.re.kr:8000/WiseNLU'
api_key='c1ec92a4-7b57-4262-9908-4e0e6d0e70dc'

param={
    'access_key':api_key,
    'argument':{
    'analysis_code':'morp',
    'text':chunk_list[0]}
    }
headers={
    'Content-Type':'application/json; charset=UTF-8'
}

res=requests.post(api_url,headers=headers,data=json.dumps(param))

res_set__=json.loads(res.text)
res_set_=res_set__['return_object']
res_set=res_set_['sentence']
big_word=[]
for data in tqdm(res_set):
    data=data['morp']
    word_set=[x['lemma'] for x in data]
    big_word.extend(word_set)

material=' '.join(big_word)
from wordcloud import WordCloud
wc=WordCloud(font_path='resource/yafont.ttf').generate(material)
plt.figure(figsize=(15,8))
plt.imshow(wc)
plt.axis("off")
plt.show()
plt.close()
