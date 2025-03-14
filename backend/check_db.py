from app import app
from models.user import User
from models import db

# Check existing users
with app.app_context():
    users = User.query.all()
    if users:
        print(f"Found {len(users)} users:")
        for user in users:
            print(f"- {user.email} (name: {user.name}, has password: {bool(user.password_hash)})")
    else:
        print("No users found in database.")
        
    # Create a test user if needed
    test_email = "123@gmail.com"
    test_user = User.query.filter_by(email=test_email).first()
    
    if not test_user:
        print(f"Creating test user with email {test_email} and password 'alexander21'")
        new_user = User(email=test_email, name="Test User")
        new_user.set_password("alexander21")
        db.session.add(new_user)
        db.session.commit()
        print("Test user created successfully")
    else:
        print(f"Test user {test_email} already exists")