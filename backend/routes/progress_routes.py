from flask import Blueprint, request, jsonify
from config.db import get_db_connection
from datetime import date, datetime

progress_routes = Blueprint('progress', __name__)

@progress_routes.route('/mark-complete', methods=['POST'])
def mark_complete():
    data = request.json
    user_id = data.get('user_id')
    task_type = data.get('task_type') # 'diet' or 'workout'
    
    if not user_id or not task_type:
        return jsonify({"error": "Missing data"}), 400
        
    today = date.today().isoformat()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Check if record exists for today
        cursor.execute("SELECT * FROM user_progress WHERE user_id = %s AND entry_date = %s", (user_id, today))
        progress = cursor.fetchone()
        
        if not progress:
            # Create new record
            if task_type == 'diet':
                cursor.execute("INSERT INTO user_progress (user_id, entry_date, diet_completed) VALUES (%s, %s, %s)", (user_id, today, True))
            else:
                cursor.execute("INSERT INTO user_progress (user_id, entry_date, workout_completed) VALUES (%s, %s, %s)", (user_id, today, True))
        else:
            # Update existing record
            field = 'diet_completed' if task_type == 'diet' else 'workout_completed'
            cursor.execute(f"UPDATE user_progress SET {field} = %s WHERE user_id = %s AND entry_date = %s", (True, user_id, today))
            
        # Re-fetch for status check
        cursor.execute("SELECT diet_completed, workout_completed FROM user_progress WHERE user_id = %s AND entry_date = %s", (user_id, today))
        updated = cursor.fetchone()
        
        is_fully_done = updated['diet_completed'] and updated['workout_completed']
        
        conn.commit()
        return jsonify({
            "message": f"{task_type.capitalize()} marked as complete!",
            "fully_completed": is_fully_done
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()

@progress_routes.route('/status/<int:user_id>', methods=['GET'])
def get_progress_status(user_id):
    today = date.today().isoformat()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT diet_completed, workout_completed FROM user_progress WHERE user_id = %s AND entry_date = %s", (user_id, today))
        status = cursor.fetchone() or {"diet_completed": False, "workout_completed": False}
        
        # Calculate days planned (mock logic: days since account creation or fixed 30)
        cursor.execute("SELECT created_at FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        days_active = 1
        if user and user['created_at']:
            diff = datetime.now() - user['created_at']
            days_active = diff.days + 1
            
        return jsonify({
            "diet_completed": bool(status['diet_completed']),
            "workout_completed": bool(status['workout_completed']),
            "days_planned": 30, # Target
            "days_active": days_active
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
