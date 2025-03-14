from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import models
from models import db
from routes.auth_routes import auth_bp

app = Flask(__name__)

# Configure app
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///noir_et_or.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-secret-key') 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400  # 24 hours
app.config['CORS_HEADERS'] = 'Content-Type'

# Initialize extensions with more explicit CORS settings
CORS(app, 
     resources={r"/api/*": {"origins": "*"}},
     supports_credentials=True,
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization", "X-Requested-With", "Accept"])
jwt = JWTManager(app)
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp)

@app.route('/')
def home():
    print("Home endpoint called")
    return jsonify({'message': 'Flask Backend Connected'})

@app.after_request
def after_request(response):
    print(f"Request to {request.path} with method {request.method}")
    return response

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Use host='0.0.0.0' to accept connections from any source
    print("Starting Flask server at http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)