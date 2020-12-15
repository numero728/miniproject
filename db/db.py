import pymysql as my

def db_get_ExchangeRate():
  conn = None
  rows = None
  try:
    conn = my.connect(host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com',
                      user='admin',
                      password='pnudb960726!',
                      port=3306,
                      db='yaneodoo',
                      charset='utf8mb4', cursorclass=my.cursors.DictCursor)
        # --------------------------------------
    with conn.cursor() as cursor:
      sql = '''
            SELECT * FROM exchange_rate;
            '''
      cursor.execute(sql)
      rows = cursor.fetchall()
        # --------------------------------------
  except Exception as e:
    print('예외 발생', e)
  finally:
    if conn:
      conn.close()
    return rows


if __name__=='__main__':
  print(db_get_ExchangeRate())