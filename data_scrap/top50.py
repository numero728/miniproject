# 모듈 import
import requests
import pandas as pd
from zipfile import ZipFile
from bs4 import BeautifulSoup as BS
import lxml
import json
from sqlalchemy import create_engine
conn=0
try:
    # import pymysql
    # from sqlalchemy import create_engine
    base='http://marketdata.krx.co.kr'
    url='http://marketdata.krx.co.kr/mdi#document=0506'
    res=requests.get(url)
    source=BS(res.text,'lxml')
    data=source.select('li.depth3 a')
    df_data=[]
    for d in data:
        href=d['href']
        name=d.text
        data_id=d['data-menu-id']
        pack_data=dict([('id',data_id),('name',name),('href',base+href)])
        pack_data
        df_data.append(pack_data)

    data=pd.DataFrame(df_data,columns=['id','name','href'])
    dialect='mysql'
    db_driver='pymysql'
    username='admin'
    password='pnudb960726!'
    host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com'
    port='3306'
    database='scrap_data'
    db_url=f"{dialect}+{db_driver}://{username}:{password}@{host}:{port}/{database}"
    engine=create_engine(db_url)
    conn=engine.connect()
    data.to_sql('scrap_meta',conn,if_exists='replace',index=False)
except Exception as e:
    print(e)
finally:
    conn.close()

