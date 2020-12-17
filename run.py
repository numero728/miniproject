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
  return render_template('news.html')


@app.route('/exchange')
def exchange():
  exchange_rate = exch_query()
  return render_template('exchange.html', exchange_rate=exchange_rate)


@app.route('/index')
def index():
    curPage = 1 if not request.args.get('PageNo') else int(request.args.get('PageNo'))
    amt = 10 if not request.args.get('amt') else int(request.args.get('amt'))
    rows = db_selectIndexList(curPage, amt)
    return render_template('kospi.html', market_index=rows)


@app.route('/chat')
def chat():
  return render_template('chat.html')


if __name__ == '__main__':
  app.run(debug=True)
