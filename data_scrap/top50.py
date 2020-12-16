# 모듈 import
import requests
import pandas as pd
from zipfile import ZipFile
from bs4 import BeautifulSoup as BS
import lxml
import json
import datetime
import re
import gzip

# import pymysql
# from sqlalchemy import create_engine
base='http://marketdata.krx.co.kr/'
url='http://marketdata.krx.co.kr/mdi#document=0506'
res=requests.get(url)
source=BS(res.text,'lxml')
data=source.select('li.depth3 a')
df_data=[]
for d in data:
    href=d['href']
    name=d.text
    data_id=d['data-menu-id']
    pack_data=dict([('id',data_id),('name',name),('href',href)])
    pack_data
    df_data.append(pack_data)
    print(data.index(d))

data=pd.DataFrame(df_data,columns=['id','name','href'])
dd=data['href']
dd[0]
href=dd[0]
href='/contents/MKD/10/1003/10030600/MKD10030600.jsp'
base+href
res=requests.get(base+href)

# DB 연결 및 상장기업 목록 조회
# conn=pymysql.connect(
#     user='admin',
#     host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com',
#     port=3306,
#     password='pnudb960726!',
#     charset='utf8mb4',
#     database='scrap_data',
#     cursorclass=pymysql.cursors.DictCursor
# )
# with conn.cursor() as cursor:
#     sql="SELECT * FROM dart_api_고유번호 WHERE stock_code IS TRUE;"
#     cursor.execute(sql)
#     data=cursor.fetchall()
#     conn.close()

# pd_data=pd.DataFrame(data)
# print(pd_data)
# dialect='mysql'
# db_driver='pymysql'
# username='admin'
# password='pnudb960726!'
# host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com'
# port='3306'
# database='scrap_data'
# db_url=f"{dialect}+{db_driver}://{username}:{password}@{host}:{port}/{database}"
# engine=create_engine(db_url)
# conn=engine.connect()
# pd_data.to_sql('scrap_on',conn,if_exists='replace',index=False)
# conn.close()

