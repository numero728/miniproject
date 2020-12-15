from flask import Flask, render_template, session, make_response
from flask_socketio import SocketIO, emit
from flask_session import Session
import re
import time

search_api='AIzaSyCcsjF9lEDadtt1C76PyvEnK2jfjLAjuxk'
app=Flask(__name__)
app.config['SECRET_KEY']='miniproject'
app.config['SESSION_TYPE']='filesystem'
Session(app)
socketio=SocketIO(app,cors_allowed_origins='*', pingInterval=60000,pingTimeout=60000,async_mode='threading', manage_session=False)
msg_pack=[]
log_on=False
@socketio.on('connect')
def connect():
  print('유저가 접속하였다.')
  # if 'username' in session:
  #   emit('remain',{'user':session['username']})
  #   for i in msg_pack:
  #     emit('server_send_msg',{'user':i['user'],'msg':i['msg']})
  # else:
  #   pass

@socketio.on('client_send_name')
def client_send_name_handler(data):
  print(dir(data))
  client_name=data['client_name']
  msg=f'{client_name}님이 입장하셨습니다.'
  session['username']=client_name
  emit('system_msg',{'user':'admin','msg':msg},broadcast=True)
  if len(msg_pack)>100:
    msg_pack.pop(msg_pack[0])
    msg_pack.append({'user':'awedmin','msg':msg})
  else:
    msg_pack.append({'user':'admin','msg':msg}) 
  
@socketio.on('client_send_msg')
def client_send_msg_handler(data):
  client_name=data['client_name']
  msg=data['client_msg']
  emit('server_send_msg',{'user':client_name,'msg':msg, 'stock_code':'Null'},broadcast=True)
  if len(msg_pack)>100:
    msg_pack.pop(msg_pack[0])
    msg_pack.append({'user':client_name,'msg':msg})
  else:
    msg_pack.append({'user':client_name,'msg':msg})


@app.route('/')
def home():
    return render_template('home.html', name='사용자명')


@app.route('/news')
def news():
    return render_template('news.html', name='사용자명')


@app.route('/index')
def index():
    return render_template('index.html', name='사용자명')


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