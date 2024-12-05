from flask import Blueprint, request, jsonify
from models import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    user = cursor.fetchone()
    
    if user:
        return jsonify({'token': 'fake-jwt-token'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    id_number = data.get('id_number')
    email = data.get('email')
    phone_number = data.get('phone_number')
    password = data.get('password')
    role = data.get('role')
    profile_picture = data.get('profile_picture')
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO users (first_name, last_name, username, id_number, email, phone_number, password, role, profile_picture) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                   (first_name, last_name, username, id_number, email, phone_number, password, role, profile_picture))
    db.commit()
    
    return jsonify({'message': 'User created successfully'}), 201