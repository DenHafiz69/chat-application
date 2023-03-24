from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '8f2009a07dab679c5d31366451a955263246e5e8cf17d12ff8fbc142072feab4#'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('Message was received!')

@socketio.on('my event')
def handle_my_event(json, methods=['GET', 'POST']):
    print('Received my event: ' + str(json))
    socketio.emit('My response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)