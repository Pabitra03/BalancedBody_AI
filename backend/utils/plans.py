def get_diet_plan_details(plan_id):
    plans = {
        1: {
            "name": "Fat Loss & Metabolic Reset",
            "desc": "High thermic effect, low carb diet designed for sustainable weight loss.",
            "macros": {"protein": 40, "carbs": 25, "fats": 35},
            "monday": {"breakfast": "Oats + Banana", "lunch": "Brown Rice + Dal + Veg", "dinner": "Grilled Chicken/Paneer + Salad"},
            "tuesday": {"breakfast": "Eggs/Paneer + Toast", "lunch": "Chapati + Vegetable Curry", "dinner": "Rice + Fish/Tofu"}
        },
        2: {
            "name": "Balanced Maintenance",
            "desc": "Optimal balance of macronutrients for maintaining weight and providing sustained energy.",
            "macros": {"protein": 30, "carbs": 40, "fats": 30},
            "monday": {"breakfast": "Eggs/Paneer + Toast", "lunch": "Chapati + Vegetable Curry", "dinner": "Rice + Fish/Tofu"},
            "tuesday": {"breakfast": "Smoothie + Nuts", "lunch": "Brown Rice + Chicken/Paneer", "dinner": "Vegetable Soup + Salad"}

        },
        3: {
            "name": "Muscle Building & Strength",
            "desc": "Caloric surplus with high protein and clean carbs to fuel muscle hypertrophy.",
            "macros": {"protein": 35, "carbs": 45, "fats": 20},
            "monday": {"breakfast": "Smoothie + Nuts", "lunch": "Brown Rice + Chicken/Paneer", "dinner": "Vegetable Soup + Salad"},
            "tuesday": {"breakfast": "Oats + Apple", "lunch": "Chapati + Dal + Veg", "dinner": "Grilled Paneer/Chicken"}
        }
    }
    return plans.get(plan_id, plans[2])

def get_workout_plan_details(plan_id):
    plans = {
        1: {
            "name": "Cardio & HIIT Burn",
            "desc": "High intensity interval training combined with steady state cardio.",
            "monday": "30 min Cardio", "tuesday": "HIIT Workout", "wednesday": "Stretching", "thursday": "Cardio + Core", "friday": "Yoga", "saturday": "Full Body Burn", "sunday": "Rest"
        },
        2: {
            "name": "Hypertrophy Strength Builder",
            "desc": "Resistance training focused on progressive overload and muscle growth.",
            "monday": "Upper Body Push", "tuesday": "Lower Body Quads", "wednesday": "Rest / Active Recovery", "thursday": "Upper Body Pull", "friday": "Lower Body Glutes/Hams", "saturday": "Full Body Conventional", "sunday": "Rest"
        },
        3: {
            "name": "Functional Athlete",
            "desc": "A mix of agility, strength, and endurance for overall peak physical fitness.",
            "monday": "Full Body Strength", "tuesday": "Sprint Intervals", "wednesday": "Mobility & Core", "thursday": "Upper Body Power", "friday": "Lower Body Power", "saturday": "Long Endurance Run", "sunday": "Rest"
        }
    }
    return plans.get(plan_id, plans[2])
def get_weekly_plan(diet_id, workout_id):
    diet_details = get_diet_plan_details(diet_id)
    workout_details = get_workout_plan_details(workout_id)
    
    days = ['monday', 'tuesday', 'monday', 'tuesday', 'monday', 'tuesday', 'monday'] # Simplified mock week
    DAYS_FULL = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    weekly_plan = []
    for i in range(7):
        day_key = days[i]
        diet_day = diet_details.get(day_key, diet_details['monday'])
        weekly_plan.append({
            "day": DAYS_FULL[i],
            "breakfast": diet_day['breakfast'],
            "lunch": diet_day['lunch'],
            "dinner": diet_day['dinner'],
            "workout": workout_details.get(day_key, workout_details['monday'])
        })
    return weekly_plan
