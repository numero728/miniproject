import pandas as pd
import pickle as pik
from tqdm import tqdm 
table=pd.read_excel('data/kospi_list.xlsx')
table['종목코드']=table['종목코드'].map(lambda x: str(x).zfill(6))
kospi_list=table['종목코드'].tolist()
kospi_name=table['회사명'].tolist()
kospi_corp=[]
for x in tqdm(range(len(kospi_list))):
    tu=(kospi_list[x],kospi_name[x])
    kospi_corp.append(tu)
with open('kospi_list.pkl', 'wb') as kospkl:
    pik.dump(kospi_corp,kospkl)