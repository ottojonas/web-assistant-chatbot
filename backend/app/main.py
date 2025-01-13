from app import create_app 
from flask import jsonify, request 
from flask_cors import CORS 
from flask_socketio import SocketIO, emit 

app = create_app() 
CORS(app) 
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/api/health', methods = ["GET"])
def health_check(): 
    return jsonify(status="healthy"), 200

if __name__ == '__main__': 
    socketio.run(app, debug = True, host = '0.0.0.0', port = 5000)