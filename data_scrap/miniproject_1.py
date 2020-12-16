#!/usr/bin/env python
# coding: utf-8
# # 뉴스기사 크롤링

import pandas.io.sql as pSql
from sqlalchemy import create_engine
import sqlalchemy
import pymysql
import pandas as pd
from selenium import webdriver as wd
import platform
import time
import urllib

options=wd.ChromeOptions()
options.add_argument('headless')
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("disable-dev-shm-usage")
driver = wd.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=options)
target_site = 'https://finance.naver.com/news/'
driver.get(target_site,)

main_news = driver.find_elements_by_css_selector('div.main_news > ul > li')

main_news_list = list()
for news in main_news:
    target = news.find_element_by_tag_name('a')
    main_news_dic = {
        'title': target.get_attribute('title'), 'href': target.get_attribute('href')
    }
    main_news_list.append(main_news_dic)


df = pd.DataFrame(main_news_list)

protocal = 'mysql+pymysql'
user = 'admin'
password = 'pnudb960726!'
domain = 'personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com'
port = 3306
database = 'yaneodoo'
db_url = f'{protocal}://{user}:{password}@{domain}:{port}/{database}'


engine = create_engine(db_url, encoding='utf8')
conn = engine.connect()

df.to_sql(name='main_news', con=conn, if_exists='append', index=False)

conn.close()

driver.close()
driver.quit()
