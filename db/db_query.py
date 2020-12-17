import pymysql


def news_query():
    conn=0
    try:
        conn=pymysql.connect(
            host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com',
            user='admin',
            password='pnudb960726!',
            port=3306,
            db='yaneodoo',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)


        with conn.cursor() as cursor:
            sql=f"SELECT * FROM main_news;"
            cursor.execute(sql)
            data=cursor.fetchall()
    except Exception as e:
        data=str(e)
    finally:
        conn.close()
        return(data)

def main_news_query():
    conn=0
    try:
        conn=pymysql.connect(
            host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com',
            user='admin',
            password='pnudb960726!',
            port=3306,
            db='yaneodoo',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)


        with conn.cursor() as cursor:
            sql=f"SELECT * FROM main_news2;"
            cursor.execute(sql)
            data=cursor.fetchall()
    except Exception as e:
        data=str(e)
    finally:
        conn.close()
        return(data)

def sector_query(sector,pageNo):
    conn=0
    sector_book={'elec':'전기','stock':'증시','bond':'채권'}
    try:
        conn=pymysql.connect(
            host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com',
            user='admin',
            password='pnudb960726!',
            port=3306,
            db='yaneodoo',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)


        with conn.cursor() as cursor:
            sql=f"SELECT * FROM main_news WHERE title LIKE '%{sector_book[sector]}%' LIMIT {str(int(pageNo)-1)},10;"
            print(sql)
            cursor.execute(sql)
            data=cursor.fetchall()
    except Exception as e:
        data=str(e)
    finally:
        conn.close()
        return(data)

def exch_query():
    conn=0
    try:
        conn=pymysql.connect(
            host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com',
            user='admin',
            password='pnudb960726!',
            port=3306,
            db='yaneodoo',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)


        with conn.cursor() as cursor:
            sql=f"SELECT * FROM exchange_rate;"
            cursor.execute(sql)
            data=cursor.fetchall()
    except Exception as e:
        data=str(e)
    finally:
        conn.close()
        return(data)


def index_query():
    conn=0
    try:
        conn=pymysql.connect(
            host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com',
            user='admin',
            password='pnudb960726!',
            port=3306,
            db='scrap_data',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)


        with conn.cursor() as cursor:
            sql=f"SELECT * FROM market_index;"
            cursor.execute(sql)
            data=cursor.fetchall()
    except Exception as e:
        data=str(e)
    finally:
        conn.close()
        return(data)

def db_selectIndexList(curPageId=1, onePage_dataNum=10):
    conn = None
    rows = None
    try:
        conn = pymysql.connect(host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com',
                          user='admin',
                          password='pnudb960726!',
                          port=3306,
                          db='scrap_data',
                          charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        # --------------------------------------
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM market_index LIMIT %s, %s;'
            # 한페이지에서 보여지는 데이터의 총 수
            amt = onePage_dataNum
            # 데이터를 가져오는 row상의 시작 위치
            startPage = (curPageId - 1) * amt
            cursor.execute(sql, (startPage, amt))
            # 결과를 다 가져와라
            rows = cursor.fetchall()
        # --------------------------------------
    except Exception as e:
        print('예외 발생', e)
    finally:
        if conn:
            conn.close()
    return rows



def youtube_query():
    conn=0
    try:
        conn=pymysql.connect(
            host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com',
            user='admin',
            password='pnudb960726!',
            port=3306,
            db='yaneodoo',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)


        with conn.cursor() as cursor:
            sql=f"SELECT * FROM youtube;"
            cursor.execute(sql)
            data=cursor.fetchall()
    except Exception as e:
        data=str(e)
    finally:
        conn.close()
        return(data)
    

if __name__ == '__main__':
    data=index_query()
    print(db_selectIndexList())