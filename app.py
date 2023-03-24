# Import Flask and render_template module. render_template is used to render the webpages
from flask import Flask, render_template

# Import socketIO and send module from flask_socketIO
from flask_socketio import SocketIO, send

# Creates a new Flask app instance
app = Flask(__name__)
app.config['SECRET'] = "secret!123" # Sets a secret key, this is used to keep the client sessions secure
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print("Received message: " + message)
    if message != "User connected!":
        send(message, broadcast=True)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)