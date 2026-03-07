def get_diet_plan_details(plan_id, diet_type='non_vegetarian'):
    is_veg = diet_type == 'vegetarian'
    img_path = "assets/img/"
    
    plans = {
        1: {
            "name": "Fat Loss & Metabolic Reset",
            "desc": "High thermic effect diet designed for sustainable fat loss while maintaining muscle.",
            "macros": {"protein": 40, "carbs": 25, "fats": 35},
            "monday": {
                "breakfast": {
                    "item": ("Poha with Sprouts & Pomegranate" if is_veg else "Avocado & Egg Sourdough Toast"),
                    "image": (img_path + "veg_breakfast.png" if is_veg else img_path + "non_veg_breakfast.png"),
                    "details": "Rich in complex carbs and healthy fats to kickstart your metabolism."
                },
                "lunch": {
                    "item": "Brown Rice with Mixed Dal & Sauteed Veggies",
                    "image": img_path + "veg_main.png",
                    "details": "Fiber-rich meal with complete plant-based proteins."
                },
                "dinner": {
                    "item": ("Grilled Malai Paneer with Garden Salad" if is_veg else "Grilled Lemon-Herb Chicken with Quinoa"),
                    "image": (img_path + "veg_main.png" if is_veg else img_path + "non_veg_main.png"),
                    "details": "Low carb, high protein dinner for optimal recovery."
                }
            },
            "tuesday": {
                "breakfast": {
                    "item": ("Paneer & Veggie Scramble" if is_veg else "Boiled Eggs with Sweet Potato"),
                    "image": (img_path + "veg_breakfast.png" if is_veg else img_path + "non_veg_breakfast.png"),
                    "details": "Quick and easy high-protein start to the day."
                },
                "lunch": {
                    "item": ("Soya Chunks Curry with Whole Wheat Chapati" if is_veg else "Tuna Salad with Chickpeas"),
                    "image": (img_path + "veg_main.png" if is_veg else img_path + "non_veg_main.png"),
                    "details": "Lean protein source to keep you full through the afternoon."
                },
                "dinner": {
                    "item": ("Tofu Stir-fry with Broccoli & Mushrooms" if is_veg else "Pan-seared Salmon with Asparagus"),
                    "image": (img_path + "veg_main.png" if is_veg else img_path + "non_veg_main.png"),
                    "details": "Omega-3 rich meal for heart health and inflammation control."
                }
            }
        },
        2: {
            "name": "Balanced Maintenance",
            "desc": "Optimal macronutrient balance for stable energy and weight maintenance.",
            "macros": {"protein": 30, "carbs": 40, "fats": 30},
            "monday": {
                "breakfast": {
                    "item": ("Paneer Paratha with Greek Yogurt" if is_veg else "Moong Dal Chilla with Eggs"),
                    "image": (img_path + "veg_breakfast.png" if is_veg else img_path + "non_veg_breakfast.png"),
                    "details": "Traditional balanced breakfast with a modern healthy twist."
                },
                "lunch": {
                    "item": "Whole Wheat Chapati with Vegetable Curry & Curd",
                    "image": img_path + "veg_main.png",
                    "details": "Standard balanced Indian meal for sustained energy."
                },
                "dinner": {
                    "item": ("Mix Veg Khichdi with Paneer" if is_veg else "Brown Rice with Fish Curry"),
                    "image": (img_path + "veg_main.png" if is_veg else img_path + "non_veg_main.png"),
                    "details": "Easy to digest dinner that promotes good sleep."
                }
            },
            "tuesday": {
                "breakfast": {
                    "item": "Berry & Nut Smoothie with Whey/Plant Protein",
                    "image": img_path + "veg_breakfast.png",
                    "details": "Antioxidant-rich quick breakfast for busy mornings."
                },
                "lunch": {
                    "item": ("Paneer Tikki with Mint Chutney & Salad" if is_veg else "Chicken Caesar Salad (No Mayo)"),
                    "image": (img_path + "veg_main.png" if is_veg else img_path + "non_veg_main.png"),
                    "details": "Light yet protein-dense lunch."
                },
                "dinner": {
                    "item": "Vegetable Soup with Grilled Mushrooms & Corn",
                    "image": img_path + "veg_main.png",
                    "details": "Low calorie, high volume meal to prevent late-night cravings."
                }
            }
        },
        3: {
            "name": "Muscle Building & Strength",
            "desc": "Caloric surplus with high protein and clean carbs to fuel muscle hypertrophy.",
            "macros": {"protein": 35, "carbs": 45, "fats": 20},
            "monday": {
                "breakfast": {
                    "item": "Peanut Butter & Banana Sourdough with Seeds",
                    "image": img_path + "veg_breakfast.png",
                    "details": "Power-packed caloric-dense start for heavy training days."
                },
                "lunch": {
                    "item": ("Brown Rice with Paneer Butter Masala (Low Fat)" if is_veg else "Chicken Breast with Sweet Potato Fries"),
                    "image": (img_path + "veg_main.png" if is_veg else img_path + "non_veg_main.png"),
                    "details": "High quality carbs and protein for muscle glycogen refilling."
                },
                "dinner": {
                    "item": ("Lentil Burger with Grilled Paneer" if is_veg else "Beef/Turkey Mince with Whole Wheat Pasta"),
                    "image": (img_path + "veg_main.png" if is_veg else img_path + "non_veg_main.png"),
                    "details": "Heavy protein load for overnight muscle synthesis."
                }
            },
            "tuesday": {
                "breakfast": {
                    "item": "Oats with Walnuts, Honey & Apple",
                    "image": img_path + "veg_breakfast.png",
                    "details": "Slow-releasing carbs for long-lasting energy."
                },
                "lunch": {
                    "item": "Whole Wheat Pav with Sprouted Moong/Egg Bhurji",
                    "image": (img_path + "veg_main.png" if is_veg else img_path + "non_veg_breakfast.png"),
                    "details": "Nutrient-dense meal with high bioavailability."
                },
                "dinner": {
                    "item": ("Grilled Paneer Steaks with Mashed Potatoes" if is_veg else "Grilled Fish with Garlic Roasted Broccoli"),
                    "image": (img_path + "veg_main.png" if is_veg else img_path + "non_veg_main.png"),
                    "details": "Post-workout recovery champion."
                }
            }
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

def get_weekly_plan(diet_id, workout_id, diet_type='non_vegetarian'):
    diet_details = get_diet_plan_details(diet_id, diet_type)
    workout_details = get_workout_plan_details(workout_id)
    
    days = ['monday', 'tuesday', 'monday', 'tuesday', 'monday', 'tuesday', 'monday'] # Simplified mock week
    DAYS_FULL = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    weekly_plan = []
    for i in range(7):
        day_key = days[i]
        diet_day = diet_details.get(day_key, diet_details['monday'])
        weekly_plan.append({
            "day": DAYS_FULL[i],
            "breakfast": diet_day['breakfast']['item'],
            "lunch": diet_day['lunch']['item'],
            "dinner": diet_day['dinner']['item'],
            "diet_image": diet_day['lunch']['image'], # Primary image for the day
            "workout": workout_details.get(day_key, workout_details['monday'])
        })
    return weekly_plan
