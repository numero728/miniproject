#!/usr/bin/env python
# coding: utf-8

# In[82]:


# 유튜브 크롤링
from selenium import webdriver as wd
import platform
import time
import urllib


# In[83]:


# 2. 브라우저 띄우기
driver = wd.Chrome('./chromedriver.exe')


# In[84]:


# 3. 접속
keyword = urllib.parse.quote('주식') 
target_site = f'https://www.youtube.com/results?search_query={keyword}&sp=CAMSBAgCEAE%253D'
# https://www.youtube.com/results?search_query=%EC%A3%BC%EC%8B%9D&sp=CAMSBAgCEAE%253D


# In[85]:


driver.get( target_site )


# In[86]:


# 4. 더보기 액션을 작동시켜서, 1일치 데이터를 전부 로드한다
#    상위버전 -> 더보기 통신 프로토콜을 분석하여 직접 호출한다(조심, 많은 검토 필요)
# 스크롤 바를 밑으로 내리는 행위, 스크립트에서 스크롤 이동 처리
for n in range(5): # 5회 정도만 내리겠다(설정)
    # 현재 화면에서 스크립트를 가동
    # 1000넉넉하게 크기를 잡은 것
    driver.execute_script('''
        window.scrollBy(0, 1000)
    ''')
    time.sleep(2)


# In[87]:


# 5. 썸네일, 제목, 링크, 조회수, 업로드시간, 게시자, 영상요약, 댓글 수집
#    영상의 메타 데이터 수집
#    검색결과는 ytd-video-renderer 태그를 모으면 된다
videos = driver.find_elements_by_tag_name('ytd-video-renderer')
len( videos )


# In[88]:


# 일 조회수 상위 20건만 진행
for video in videos[:20]:
    # 제목
    target = video.find_element_by_id('video-title')
    title  = target.get_attribute('title')
    # 썸네일
    thumbnail = video.find_element_by_id('img').get_attribute('src')
    # 링크
    video_url = target.get_attribute('href')
    print( title, thumbnail, video_url )


# In[90]:


youtube_list = list()
for video in videos[:20]:  
    target    = video.find_element_by_id('video-title')# 제목 a태그, 링크를 가진 곳
    title     = target.get_attribute('title')
    thumbnail = video.find_element_by_id('img').get_attribute('src')    
    video_url = target.get_attribute('href')
    # 데이터 수집
    youtube_list.append( {
        't':title,
        'n':thumbnail,
        'v':video_url
    } )
youtube_list


# In[48]:


# # 리뷰 로드
# for page in video_metas[:1]:
#     driver.get( page['v'] )
#     time.sleep(5)
#     # 리뷰를 모두 로드하기 위해서 컨텐츠를 스크롤한다
#     for n in range(10):
#         driver.execute_script('''
#             window.scrollBy(0, 1000)
#         ''')
#         time.sleep(2)
#     # 리뷰 수집
#     reviews = driver.find_elements_by_tag_name('ytd-comment-thread-renderer')
#     for review in reviews:
#         print('-'*100)
#         # 해당 요소 밑에 있는 모든 텍스트를 가져오시오
#         print( review.text  )
#         print('-'*100)


# In[91]:


# 데이터 적재 프레임 만들기
import pandas as pd
import pymysql
import sqlalchemy


# In[92]:


df = pd.DataFrame(youtube_list)


# In[93]:


from sqlalchemy import create_engine
import pandas.io.sql as pSql


# In[94]:


protocal = 'mysql+pymysql'
user     = 'admin'
password = 'pnudb960726!'
domain   = 'personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com'
port = 3306
database = 'yaneodoo'
db_url = f'{protocal}://{user}:{password}@{domain}:{port}/{database}'


# In[95]:


engine = create_engine(db_url, encoding = 'utf8')


# In[96]:


conn = engine.connect()


# In[97]:


df.to_sql(name = 'youtube', con = conn, if_exists ='replace',index = False)


# In[98]:


conn.close()


# In[99]:


driver.close()
driver.quit()


# In[ ]:





# In[ ]:




