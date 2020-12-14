from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit
import re
import time
import requests

search_api='AIzaSyCcsjF9lEDadtt1C76PyvEnK2jfjLAjuxk'
app=Flask(__name__)
app.secret_key='miniproject'
socketio=SocketIO(app,ping_timeout=60,ping_intervla=50,cors_allowed_origins='*', async_mode='threading')
msg_pack=[]

@socketio.on('connect')
def connect():
  print('유저가 접속하였다.')

@socketio.on('client_send_name')
def client_send_name_handler(data):
  print(dir(data))
  client_name=data['client_name']
  msg=f'{client_name}님이 입장하셨습니다.'
  emit('system_msg',{'user':'admin','msg':msg},broadcast=True)
  msg_pack.append({'user':'admin','msg'})

@socketio.on('client_send_msg')
def client_send_msg_handler(data):
  client_name=data['client_name']
  msg=data['client_msg']
  stock_code=re.match(r'([0-9]6)',msg).group(0)
  emit('server_send_msg',{'user':client_name,'msg':msg, 'stock_code'=stock_code},broadcast=True)
  time.sleep(1)


@app.route('/chat')
def chat():
  return render_template('chat.html')

if __name__=='__main__':
  socketio.run(app, debug=True)