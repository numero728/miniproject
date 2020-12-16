from sqlalchemy import create_engine
import pymysql
import pickle
import yfinance as yf
from tqdm import tqdm
import pandas as pd

with open('kospi_list.pkl', 'rb') as listpkl:
    data=pickle.load(listpkl)

db_url="mysql+pymysql://admin:pnudb960726!@personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com:3306/hist_data"

for i,j in tqdm(data[256:]):
    code=str(i)+'.KS'
    tick=yf.Ticker(code)
    conn=0
    try:
        hist=tick.history(period='Max')
    except Exception as e:
        print(e)
        hist=pd.DataFrame(['Error'],columns=['Status'])
    try:
        engine=create_engine(db_url)
        conn=engine.connect()
        hist.to_sql(str(i)+' '+j,conn,if_exists='replace',index=True)
    except:
        with open(str(i)+' '+j+'.pkl','wb') as pk:
            pickle.dump(hist,pk)
    finally:
        conn.close()


