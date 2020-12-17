from flask import Flask, render_template, request, url_for, session
from db.db_query import *
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config['SECRET_KEY'] = 'miniproject'

# socketio 통신 관련
if True:
    socketio = SocketIO(app, cors_allowed_origins='*', pingInterval=600000,
                        pingTimeout=600000, async_mode='threading', manage_session=False)
    msg_pack = []

    # 2. 유저 접속 수신
    @socketio.on('connect')
    def connect():
        print('유저 접속')

    # 4. 유저 송신한 닉네임 수신 및 시스템 메시지 송신

    @socketio.on('username')
    def username(data):
        username = data['username']
        msg = f'{username}님이 입장하셨습니다.'
        emit('s_send_msg', {'user': 'admin', 'msg': msg}, broadcast=True)

    # 7. 유저 송신한 메시지 수신 및 중계

    @socketio.on('c_send_msg')
    def c_send_msg(data):
        username = data['username']
        msg = data['msg']
        emit('s_send_msg', {'user': username, 'msg': msg}, broadcast=True)

    # 9. 유저 이탈

    @socketio.on('disconnect')
    def disconnect():
        print('유저 이탈')


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


@app.route('/youtube')
def youtube():
    data = youtube_query()
    return render_template('youtube.html', youtube=data)


if __name__ == '__main__':
    app.run(debug=True)
