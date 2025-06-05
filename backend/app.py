from flask import Flask, request, session
import secrets
from models import db,User, Admin, ParkingLot, ParkingSpot, Reservation
from flask_migrate import Migrate
from flask import jsonify
from werkzeug.security import check_password_hash
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from werkzeug.security import generate_password_hash
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS
from sqlalchemy.exc import SQLAlchemyError
from flask_caching import Cache
from flask import Flask, current_app


app = Flask(__name__)   
app.secret_key = secrets.token_hex(16)


# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///C:/Users/HP/Desktop/vehicle_parking.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize the database
db.init_app(app)
m = Migrate(app,db)

cache = Cache(app, config={'CACHE_TYPE': 'RedisCache', 'CACHE_REDIS_URL': "redis://localhost:6379/0"})
cache.init_app(app)


CORS(app, resources={r"/*": {"origins": "http://localhost:8000"}})

# Create tables (Only needed on the first run)
# with app.app_context():
#     try:
#         db.create_all()
#         print("Tables created successfully")
#     except Exception as e:
#         print(f"Error creating tables: {e}")

      
      

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/api/login', methods=['POST'])
def login():
    # Get login credentials from the request
    email = request.json.get('email')
    password = request.json.get('password')
    
    if not email or not password:
        return jsonify({'success': False, 'message': 'Email and password are required'}), 400

    # Check for the user in the Admin table
    admin = Admin.query.filter_by(email=email).first()
    if admin and check_password_hash(admin.password, password):
        return jsonify({'success': True, 'role': 'admin', 'message': 'Login successful!'}), 200

    # Check for the user in the Customer table
    customer = User.query.filter_by(email=email).first()
    if customer and check_password_hash(customer.password, password):
        return jsonify({'success': True, 'role': 'customer', 'message': 'Login successful!'}), 200

    # If no match is found
    return jsonify({'success': False, 'message': 'Invalid credentials. Please try again.'}), 401

# Route to logout
@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('customer_id', None)  # Clear the session
    return jsonify({'message': 'Logged out successfully'}), 200


@app.route('/api/customer_register', methods=['POST'])
def register_customer():
    data = request.get_json()
    # Validate incoming data
    required_fields = ['email', 'password', 'full_name', 'address', 'pincode']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400
    
    # Check if email already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400

    # Hash the password before storing
    hashed_password = generate_password_hash(data['password'])

    new_customer = User(
        email=data['email'],
        password=hashed_password,
        full_name=data['full_name'],
        address=data['address'],
        pincode=data['pincode'],
        role='user'
    )

    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({"message": "Registration successful!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Error saving customer details. Please try again."}), 500

if __name__ == '__main__':
    app.run(debug=True)