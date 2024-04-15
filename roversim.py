from flask_socketio import SocketIO
rasp: bool
try:
    import motors
    rasp = True
except:
    rasp = False

socketio: SocketIO

def init(s: SocketIO):
    global socketio
    socketio = s


def set_motion(movement: dict[str, float]):
    global socketio
    socketio.emit('set-speed', movement)

    if rasp:
        motors.acc(movement['speed']) # type: ignore
        motors.turn(movement['turn']) # type: ignore
