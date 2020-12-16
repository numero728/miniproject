# 모듈 import


from flask import Flask, render_template, session, make_response, url_for, redirect, request, jsonify
from flask_socketio import SocketIO, emit
import re
import time
from DB.db_query import *



# app 생성 및 환경설정


app=Flask(__name__)
app.config['SECRET_KEY']='miniproject'
users=[]

# socketio 객체 생성


socketio=SocketIO(app,cors_allowed_origins='*', pingInterval=600000,pingTimeout=600000,async_mode='threading', manage_session=False)



msg_pack=[]

dir(socketio)



# socketio 통신 관련
if True:

  # 2. 유저 접속 수신
  @socketio.on('connect')
  def connect():
    print('유저 접속')



  # 4. 유저 송신한 닉네임 수신 및 시스템 메시지 송신
  @socketio.on('username')
  def username(data):
    username=data['username']
    msg=f'{username}님이 입장하셨습니다.'
    emit('system_msg',{'user':'admin','msg':msg},broadcast=True)


  # 7. 유저 송신한 메시지 수신 및 중계
  @socketio.on('c_send_msg')
  def c_send_msg(data):
    username=data['username']
    msg=data['msg']
    emit('s_send_msg',{'user':username,'msg':msg},broadcast=True)


  # 9. 유저 이탈
  @socketio.on('disconnect')
  def disconnect():
    print('유저 이탈')


if True:
  @app.route('/')
  def home():
      return render_template('home.html', name='사용자명')

  @app.route('/news')
  def news():
      data=news_query()
      return render_template('news.html', result=data)

  @app.route('/exchange')
  def exchange():
      data=exch_query()
      data_body=[]
      for d in data:
        d.pop('info_link')
        data_body.append(d)
      data=data_body
      return render_template('exchange.html', result=data)

  @app.route('/index')
  def index():
    data=index_query()
    list(data[0].keys())
    data_body=[]
    for d in data:
      k=list(d.keys())
      v=list(d.values())
      k=k[0:9]
      v=v[0:9]
      kv=dict(zip(k,v))
      data_body.append(kv)
    data=data_body
    return render_template('index.html', result=data)

  @app.route('/youtube')
  def youtube():
      data=youtube_query()
      return render_template('youtube.html', result=data)

  @app.route('/test')
  def test():
      return render_template('test.html')


  @app.route('/chat')
  def chat():
    if 'username' in session:
      print('''
      
      
      
      
      
      
      
      테스트
      
      
      
      
      
      
      
      
      
      ''')
      return render_template('chat.html', reconnect='True')
    else:
      return render_template('chat.html', reconnect='False')

  


if __name__=='__main__':
  socketio.run(app, debug=True)



