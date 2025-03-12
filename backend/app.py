from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

@app.route('/')
def home():
    return jsonify({'message': 'Flask Backend Connected'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
