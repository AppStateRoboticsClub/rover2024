import json
from flask import Flask, render_template
from flask_socketio import SocketIO

controls: dict[str, float] = {
    'w': 0
}

motion: dict[str, float] = {
    'speed': 0,
    'turn': 0
}

motion1: dict[str, float] = {
    'speed': 0,
    'turn': 0
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

# @socketio.on('message')
# def handle_message(data):
#     print('Received message:', data)
#     socketio.emit('response', 'Server received your message: ' + data)

@socketio.on('key-down')
def handle_key(data, m = 1):
    print(motion)
    if data == 'w':
        motion['speed'] = -0.75 * m
    if data == 's':
        motion['speed'] = 0.75 * m
    if data == 'a':
        motion['turn'] = -1 * m
    if data == 'd':
        motion['turn'] = 1 * m
    print(motion)
    update_motion()

@socketio.on('key-up')
def handle_key_up(data):
    handle_key(data, 0)

def update_motion():
    if motion.values() == motion1.values():
        print("smile")
        return
    for key in list(motion.keys()):
        motion_old = motion[key]
    socketio.emit('set-speed', {"speed": motion['speed'], "turn": motion['turn']})

if __name__ == '__main__':
    socketio.run(app, debug=True) # type: ignore