#!/usr/bin/env python
# coding: utf-8

# In[13]:


from bs4 import BeautifulSoup
import html5lib
import requests
from datetime import datetime


# In[14]:


now_date = datetime.today().strftime("%Y-%m-%d")
# print(now_date)


# In[15]:


target_site = f'https://finance.naver.com/news/mainnews.nhn?date={now_date}'
# 웹 스크래핑
res = requests.get(target_site)


# In[20]:


soup = BeautifulSoup(res.text, 'html5lib')


# In[21]:


main_news = soup.select('div.mainNewsList > ul > li')


# In[54]:


results = list()
for news in main_news:
    if not news.a.string:
        tmp = news.select_one('dl > dd.articleSubject > a')
        dic = {
            'title' : tmp.string
            ,'href': 'https://finance.naver.com' + tmp.get('href')
        }
    else:
        dic = {
            'title' : news.a.string
            ,'href': 'https://finance.naver.com' + news.a.get('href')
        }
    results.append(dic)


# In[55]:


import pandas as pd
import pymysql
import sqlalchemy
from sqlalchemy import create_engine
import pandas.io.sql as pSql


# In[56]:


protocal = 'mysql+pymysql'
user     = 'admin'
password = 'pnudb960726!'
domain   = 'personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com'
port = 3306
database = 'yaneodoo'
db_url = f'{protocal}://{user}:{password}@{domain}:{port}/{database}'


# In[57]:


df = pd.DataFrame(results)


# In[58]:


engine = create_engine(db_url, encoding = 'utf8')
conn = engine.connect()
df.to_sql(name = 'main_news3', con = conn, if_exists='replace', index=False)


# In[ ]:




