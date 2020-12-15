#!/usr/bin/env python
# coding: utf-8

# # 뉴스기사 크롤링

# In[66]:


from selenium import webdriver as wd
import platform
import time
import urllib


# In[42]:


# platform.system()


# In[73]:


driver = wd.Chrome('./chromedriver.exe')


# In[74]:


target_site = 'https://finance.naver.com/news/'


# In[75]:


driver.get(target_site)


# In[46]:


# 주요뉴스 파트 클래스 명 : main_news
# len(driver.find_elements_by_css_selector('div.main_news > ul > li'))


# In[76]:


main_news = driver.find_elements_by_css_selector('div.main_news > ul > li')


# In[77]:


main_news_list = list()
for news in main_news:
    target = news.find_element_by_tag_name('a')
    main_news_dic = {
        'title' : target.get_attribute('title')
        ,'href' : target.get_attribute('href')
    }
    main_news_list.append(main_news_dic)
# main_news_list


# # 데이터 적재위해 프레임 만들기

# In[78]:


import pandas as pd
import pymysql
import sqlalchemy


# In[80]:


df = pd.DataFrame(main_news_list)
# df


# In[33]:


from sqlalchemy import create_engine
import pandas.io.sql as pSql


# In[82]:


protocal = 'mysql+pymysql'
user     = 'admin'
password = 'pnudb960726!'
domain   = 'personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com'
port = 3306
database = 'yaneodoo'
db_url = f'{protocal}://{user}:{password}@{domain}:{port}/{database}'
# db_url


# In[63]:


engine = create_engine(db_url, encoding = 'utf8')


# In[64]:


conn = engine.connect()


# In[65]:


df.to_sql(name = 'main_news', con = conn, if_exists ='replace',index = False)


# In[61]:


conn.close()


# # driver 종료

# In[81]:


driver.close()
driver.quit()


# In[ ]:




