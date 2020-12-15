import pymysql as my

# 게시판에 한개의 페이지를 구성하는 데이터들을 조회하여 리턴한다
# 복수개의 데이터를 획득해서 리턴
# onePage_dataNum=5 : 기본적으로 5개를 한 페이지에서 보는 데이터 양으로 구성, 정수값을 넣으라는 표시
# culPageId=1 : 기본 페이지는 1페이지이다


def youtube_list(culPageId=1, onePage_dataNum=10):
    conn = None
    rows = None
    try:
        conn = my.connect(host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com',
                          user='admin',
                          password='pnudb960726!',
                          db='yaneodoo',
                          charset='utf8mb4', cursorclass=my.cursors.DictCursor)

        # -------------------------
        with conn.cursor() as cursor:
            sql = '''
                    SELECT * FROM stocks ORDER BY NAME ASC LIMIT %s, %s;
                '''
            # 한 페이지에서 보여지는 데이터의 총 수
            amt = onePage_dataNum
            # 데이터를 가져오는 row상의 시작 위치
            startPage = (culPageId - 1)*amt
            cursor.execute(sql, (startPage, amt))
            # 결과를 다 가져와라
            rows = cursor.fetchall()
        # --------------------------
    except Exception as e:
        print('예외발생', e)
    finally:
        if conn:
            conn.close()

    return rows
