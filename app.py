from flask import Flask, jsonify
from config import Config
from models import init_app, get_db
from routes import bp as auth_bp

app = Flask(__name__)
app.config.from_object(Config)

init_app(app)
app.register_blueprint(auth_bp)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to the Main API'}), 200

@app.before_request
def check_db_connection():
    try:
        db = get_db()
        db.ping(reconnect=True)
        app.logger.info('Database connection successful.')
    except Exception as e:
        app.logger.error('Database connection failed: %s', e)

if __name__ == '__main__':
    app.run(debug=True)