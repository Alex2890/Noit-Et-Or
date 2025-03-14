from flask import request, jsonify
from flask_jwt_extended import create_access_token
from models import db
from models.user import User
from google.oauth2 import id_token
from google.auth.transport import requests
import os

class AuthController:
    @staticmethod
    def register():
        data = request.get_json()
        
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email and password are required'}), 400
            
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already registered'}), 409
            
        user = User(email=data['email'], name=data.get('name', ''))
        user.set_password(data['password'])
        
        db.session.add(user)
        db.session.commit()
        
        access_token = create_access_token(identity=user.id)
        
        return jsonify({
            'message': 'User registered successfully',
            'token': access_token,
            'user': user.to_dict()
        }), 201
    
    @staticmethod
    def login():
        data = request.get_json()
        
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email and password are required'}), 400
            
        user = User.query.filter_by(email=data['email']).first()
        
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'Invalid email or password'}), 401
            
        access_token = create_access_token(identity=user.id)
        
        return jsonify({
            'message': 'Login successful',
            'token': access_token,
            'user': user.to_dict()
        }), 200
    
    @staticmethod
    def google_login():
        data = request.get_json()
        
        if not data or not data.get('credential'):
            return jsonify({'error': 'Google credential is required'}), 400
        
        # Get the response type (code or token)
        response_type = data.get('response_type', 'id_token')
        credential = data['credential']
        
        print(f"Google login with {response_type}: {credential[:15]}...")
        
        try:
            # Handle different response types
            if response_type == 'code':
                # This is an authorization code that needs to be exchanged
                print("Handling authorization code flow")
                
                # For demonstration, we'll create a user with minimal info
                # In production, you would exchange this code for tokens
                # using Google's token endpoint
                
                # Create or get user (for demo purposes)
                email = f"user-{hash(credential) % 10000}@example.com"
                user = User.query.filter_by(email=email).first()
                
                if not user:
                    user = User(
                        email=email,
                        name=f"Google User {hash(credential) % 1000}",
                        google_id=f"oauth-{hash(credential)}",
                        profile_picture="https://ui-avatars.com/api/?name=Google+User"
                    )
                    db.session.add(user)
                    db.session.commit()
                
            else:
                # This is an ID token that can be verified directly
                print("Handling ID token flow")
                
                # Verify the Google token
                idinfo = id_token.verify_oauth2_token(
                    credential, 
                    requests.Request(), 
                    os.getenv('GOOGLE_CLIENT_ID')
                )
                
                # Check if user exists
                user = User.query.filter_by(email=idinfo['email']).first()
                
                if not user:
                    # Create new user
                    user = User(
                        email=idinfo['email'],
                        name=idinfo.get('name', ''),
                        google_id=idinfo['sub'],
                        profile_picture=idinfo.get('picture', None)
                    )
                    db.session.add(user)
                    db.session.commit()
                elif not user.google_id:
                    # Update existing user with Google ID
                    user.google_id = idinfo['sub']
                    user.profile_picture = idinfo.get('picture', user.profile_picture)
                    db.session.commit()
            
            # Create access token for either flow
            access_token = create_access_token(identity=user.id)
            
            return jsonify({
                'message': 'Google login successful',
                'token': access_token,
                'user': user.to_dict()
            }), 200
            
        except Exception as e:
            print(f"Google login error: {str(e)}")
            return jsonify({'error': f'Google authentication error: {str(e)}'}), 401