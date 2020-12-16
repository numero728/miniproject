#!/usr/bin/env python
# coding: utf-8

# # BS4 main_news 

# In[133]:


from bs4 import BeautifulSoup
import html5lib
import requests


# In[134]:


target_site = 'https://finance.naver.com/news/'
res = requests.get(target_site)


# In[135]:


soup = BeautifulSoup(res.text, 'html5lib')


# In[136]:


main_news = soup.select('div.main_news > ul > li')


# In[137]:


results = list()
for news in main_news:
    dic = {
        'title' : news.a.string
        ,'href': news.a.get('href')
    }
    results.append(dic)


# In[138]:


import pandas as pd
import pymysql
import sqlalchemy
from sqlalchemy import create_engine
import pandas.io.sql as pSql


# In[139]:


protocal = 'mysql+pymysql'
user     = 'admin'
password = 'pnudb960726!'
domain   = 'personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com'
port = 3306
database = 'yaneodoo'
db_url = f'{protocal}://{user}:{password}@{domain}:{port}/{database}'


# In[140]:


df = pd.DataFrame(results)


# In[141]:


engine = create_engine(db_url, encoding = 'utf8')
conn = engine.connect()
df.to_sql(name = 'main_news2', con = conn, if_exists='replace', index=False)

