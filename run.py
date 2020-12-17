from flask import Flask, render_template, request, url_for
from db.db_query import *

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/news')
def news():
  main_news = news_query()
  news_count = len(main_news)
  print(news_count)
  return render_template('news.html', news_count = news_count, main_news = main_news)


@app.route('/exchange')
def exchange():
  exchange_rate = exch_query()
  return render_template('exchange.html', exchange_rate=exchange_rate)


@app.route('/index')
def index():
    curPage = 1 if not request.args.get('PageNo') else int(request.args.get('PageNo'))
    amt     = 10 if not request.args.get('amt') else int(request.args.get('amt'))
    rows    = db_selectIndexList(curPage, amt)
    # 서버쪽에서 전체 개수를 구해와서, amt양 대비하여 최대 페이지수를 계산해 둬야함 !!
    maxPage = 15 #임시로 값을 넣었습니다.
    return render_template('kospi.html', market_index=rows, 
    paging={'prePage':curPage == 1 if 0 else curPage-1, 'amt':amt, 
            'nextPage': 0 if curPage == maxPage else curPage+1
    })


@app.route('/chat')
def chat():
  return render_template('chat.html')


if __name__ == '__main__':
  app.run(debug=True)
