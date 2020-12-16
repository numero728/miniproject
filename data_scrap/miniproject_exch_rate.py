#!/usr/bin/env python
# coding: utf-8

# # 실시간으로 환율지표 웹 스크래핑

# In[37]:


# 1. 모듈 가져오기
from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[44]:


# 2. 타켓 사이트 접속
target_site = 'https://finance.naver.com/marketindex/exchangeList.nhn'
# 웹 스크래핑
res = urlopen(target_site)


# In[45]:


if res.getcode() != 200:
  print('사이트에 뭔가 문제가 있다 점검 필요')


# In[46]:


soup = BeautifulSoup(res, 'html5lib')


# - 환율 정보는 tbody > tr
# - 환율 class tit (tr > td) 
# - 매매기준율 .sale
# - 그 밖의 수치 정보는 tbody > tr:nth-child() > td:nth-child()

# In[47]:


results = list()
for tr in soup.select('tbody > tr'):
    dic = {
        'name' : tr.select_one('.tit').a.string.strip()
        ,'code': tr.select_one('.tit').a.get('href')[-6:-3]
        ,'info_link' : tr.select_one('.tit').a.get('href')
        ,'buy_std': tr.select_one('.sale').string.strip().replace(',','')
        ,'buy_cash': tr.select_one('td:nth-of-type(3)').string.strip().replace(',','')
        ,'sell_cash': tr.select_one('td:nth-of-type(4)').string.strip().replace(',','')
        ,'send_cash': tr.select_one('td:nth-of-type(5)').string.strip().replace(',','')
        ,'get_cash': tr.select_one('td:nth-of-type(6)').string.strip().replace(',','')
        ,'USD_rate': tr.select_one('td:nth-of-type(7)').string.strip()
    }
    results.append(dic)
results


# In[48]:


import pandas as pd
import pymysql
import sqlalchemy


# In[49]:


from sqlalchemy import create_engine
import pandas.io.sql as pSql


# In[50]:


protocal = 'mysql+pymysql'
user     = 'admin'
password = 'pnudb960726!'
domain   = 'personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com'
port = 3306
database = 'yaneodoo'
db_url = f'{protocal}://{user}:{password}@{domain}:{port}/{database}'


# In[51]:


df = pd.DataFrame(results)


# In[52]:


engine = create_engine(db_url, encoding = 'utf8')
conn = engine.connect()
df.to_sql(name = 'exchange_rate', con = conn, if_exists='replace', index=False)


# In[ ]:




