from flask import Flask
from flask_cors import CORS
from config.db import init_db
from routes.auth_routes import auth_bp
from routes.profile_routes import profile_bp
from routes.dashboard_routes import dashboard_bp
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Database (Commented out for Vercel/Production)
# try:
#     init_db()
# except Exception as e:
#     print(f"[WARNING] Could not init DB: {e}")

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(profile_bp, url_prefix='/api/user')
app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')

@app.route('/', methods=['GET'])
def home():
    return "Fitness AI Backend is running!"

if __name__ == '__main__':
    # Port 5001 used because macOS reserves 5000 for AirPlay Receiver
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
