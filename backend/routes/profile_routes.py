from flask import Blueprint, request, jsonify
from config.db import get_db_connection

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET'])
def get_profile():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
        
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
        
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM profiles WHERE user_id = %s", (user_id,))
        profile = cursor.fetchone()
        if profile:
            return jsonify(profile), 200
        else:
            return jsonify({"error": "Profile not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@profile_bp.route('/profile', methods=['POST'])
def save_profile():
    data = request.json
    user_id = data.get('user_id')
    
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
        
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
        
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO profiles (user_id, age, gender, weight, height, activity_level, goal, diet_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            age=VALUES(age), gender=VALUES(gender), weight=VALUES(weight),
            height=VALUES(height), activity_level=VALUES(activity_level), goal=VALUES(goal),
            diet_type=VALUES(diet_type)
        """, (
            user_id, data.get('age'), data.get('gender'), data.get('weight'), 
            data.get('height'), data.get('activity_level'), data.get('goal'),
            data.get('diet_type')
        ))
        conn.commit()
        return jsonify({"message": "Profile saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()
