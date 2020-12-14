from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit


app=Flask(__name__)
app.secret_key='miniproject'
socketio=SocketIO(app,cors_allowed_origins='*', async_mode='threading')

@socketio.on('connect')
def connect():
  print('유저가 접속하였다.')

@socketio.on('client_send_name')
def client_send_name_handler(data):
  print(dir(data))
  client_name=data['client_name']
  emit('server_send_msg',{'user':'admin','msg':f'{client_name}님이 입장하셨습니다.'},broadcast=True)

@app.route('/chat')
def chat():
  return render_template('chat.html')

if __name__=='__main__':
  socketio.run(app, debug=True)