def get_diet_plan_details(plan_id, diet_type='non_vegetarian'):
    is_veg = diet_type == 'vegetarian'
    img_path = "/assets/img/"
    
    plans = {
        1: {
            "name": "Fat Loss & Metabolic Reset",
            "desc": "High thermic effect diet designed for sustainable fat loss while maintaining muscle.",
            "macros": {"protein": 40, "carbs": 25, "fats": 35},
            "monday": {
                "breakfast": {"item": ("Poha with Sprouts" if is_veg else "Egg Bhurji with Toast"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Rich in complex carbs to start your day."},
                "lunch": {"item": ("Brown Rice & Dal" if is_veg else "Chicken Kathi Roll"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Fiber-rich meal with complete proteins."},
                "dinner": {"item": ("Grilled Paneer" if is_veg else "Grilled Chicken"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "High protein, low carb for recovery."}
            },
            "tuesday": {
                "breakfast": {"item": ("Paneer Scramble" if is_veg else "Boiled Eggs"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Quick high-protein start."},
                "lunch": {"item": ("Soya Curry" if is_veg else "Fish Tikka Salad"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Lean protein for afternoon energy."},
                "dinner": {"item": ("Tofu Masala" if is_veg else "Tandoori Fish"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Omega-3 rich for inflammation control."}
            },
            "wednesday": {
                "breakfast": {"item": "Daliya with Nuts", "image": img_path + "veg_breakfast.png", "details": "Slow-release carbs for steady energy."},
                "lunch": {"item": ("Chana Chaat" if is_veg else "Chicken Kathi Roll"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "High fiber and protein lunch."},
                "dinner": {"item": ("Moong Dal Soup" if is_veg else "Chicken Tikka Masala"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Light and easy to digest."}
            },
            "thursday": {
                "breakfast": {"item": ("Besan Chilla" if is_veg else "Omelette with Toast"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Traditional protein-rich breakfast."},
                "lunch": {"item": ("Bajra Khichdi" if is_veg else "Chicken Biryani (Clean)"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Nutrient-dense ancient grains."},
                "dinner": {"item": ("Mix Veg Curry" if is_veg else "Fish Curry"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Micronutrient-rich evening meal."}
            },
            "friday": {
                "breakfast": {"item": ("Fruit & Dahi" if is_veg else "Fruit & Dahi"), "image": img_path + "veg_breakfast.png", "details": "Probiotic-rich refreshing start."},
                "lunch": {"item": ("Paneer Salad" if is_veg else "Egg Salad with Veggies"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Low calorie, high satiety."},
                "dinner": {"item": ("Soya Chunks Stir-fry" if is_veg else "Prawn Masala"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Metabolism boosting light dinner."}
            },
            "saturday": {
                "breakfast": {"item": ("Moong Dal Chilla" if is_veg else "Scrambled Eggs with Roti"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Complex carb loaded breakfast."},
                "lunch": {"item": ("Palak Paneer with Roti" if is_veg else "Malabar Fish Curry"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Clean fats and quality protein."},
                "dinner": {"item": ("Paneer Tikka" if is_veg else "Chicken Korma"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Muscle repair focusing meal."}
            },
            "sunday": {
                "breakfast": {"item": ("Rava Idli with Sambar" if is_veg else "Rava Idli with Sambar"), "image": img_path + "veg_breakfast.png", "details": "Weekend treat without the guilt."},
                "lunch": {"item": "Mixed Veg Kurma", "image": img_path + "veg_main.png", "details": "Vitamin-packed weekend lunch."},
                "dinner": {"item": ("Rasam or Dal Shorba" if is_veg else "Chicken Clear Soup"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Detoxifying and light dinner."}
            }
        },
        2: {
            "name": "Balanced Maintenance",
            "desc": "Optimal macronutrient balance for stable energy and weight maintenance.",
            "monday": {
                "breakfast": {"item": ("Paneer Paratha" if is_veg else "Eggs & Moong Dal Chilla"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Balanced protein and energy bowl."},
                "lunch": {"item": ("Chapati & Veg Curry" if is_veg else "Chapati & Veg Curry"), "image": img_path + "veg_main.png", "details": "Standard balanced energy lunch."},
                "dinner": {"item": ("Mix Veg Khichdi" if is_veg else "Fish Curry & Rice"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Easily digestible for sleep."}
            },
            "tuesday": {
                "breakfast": {"item": "Banana Lassi", "image": img_path + "veg_breakfast.png", "details": "Antioxidant-rich quick meal."},
                "lunch": {"item": ("Paneer Tikki" if is_veg else "Chicken Tikka Chaat"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Light yet protein dense."},
                "dinner": {"item": "Tomato Soup", "image": img_path + "veg_main.png", "details": "Prevents late-night cravings."}
            },
            "wednesday": {
                "breakfast": {"item": ("Sprouted Moong Salad" if is_veg else "Egg White Omelette"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Enzyme-rich morning start."},
                "lunch": {"item": "Rajma Chawal", "image": img_path + "veg_main.png", "details": "High protein plant-based lunch."},
                "dinner": {"item": ("Kadai Paneer" if is_veg else "Chicken Tandoori"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Balanced recovery meal."}
            },
            "thursday": {
                "breakfast": {"item": ("Ragi Malt" if is_veg else "Dahi with Fruits"), "image": img_path + "veg_breakfast.png", "details": "Calcium-rich morning fuel."},
                "lunch": {"item": ("Brown Rice & Kadhi" if is_veg else "Lemon Chicken with Rice"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Probiotic-rich and energizing."},
                "dinner": {"item": ("Shakarkandi Chaat" if is_veg else "Fish Amritsari"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Fiber and Omega-3 balance."}
            },
            "friday": {
                "breakfast": {"item": "Sabza Seeds in Milk", "image": img_path + "veg_breakfast.png", "details": "Hydration and fiber focus."},
                "lunch": {"item": ("Paneer Bhurji with Rotis" if is_veg else "Pomfret Fry"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Satisfying protein-rich lunch."},
                "dinner": {"item": ("Veg Biryani" if is_veg else "Chicken Chettinad"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Comforting yet clean dinner."}
            },
            "saturday": {
                "breakfast": {"item": ("Vegetable Upma" if is_veg else "Egg Curry with Chapati"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Slow energy release for the weekend."},
                "lunch": {"item": "Kachumber Salad with Nuts", "image": img_path + "veg_main.png", "details": "Vitamin and micronutrient load."},
                "dinner": {"item": ("Matar Mushroom with Roti" if is_veg else "Chicken Seekh Kebab"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Rich in flavor, clean in macros."}
            },
            "sunday": {
                "breakfast": {"item": "Dalia with Milk", "image": img_path + "veg_breakfast.png", "details": "The classic weekend morning."},
                "lunch": {"item": "Palak Paneer Roti Wrap", "image": img_path + "veg_main.png", "details": "Portable and nutrient-dense."},
                "dinner": {"item": "Vegetable Soup", "image": img_path + "veg_main.png", "details": "Light finish to the week."}
            }
        },
        3: {
            "name": "Muscle Building & Strength",
            "desc": "Caloric surplus with high protein and clean carbs to fuel muscle hypertrophy.",
            "monday": {
                "breakfast": {"item": "Peanut Butter & Banana on Roti", "image": img_path + "veg_breakfast.png", "details": "Power-packed for training days."},
                "lunch": {"item": ("Paneer Butter Masala" if is_veg else "Butter Chicken with Sweet Potato"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Muscle glycogen refueling."},
                "dinner": {"item": ("Rajma Tikki Burger" if is_veg else "Chicken Keema with Paratha"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "High protein load for overnight synthesis."}
            },
            "tuesday": {
                "breakfast": {"item": "Masala Oats", "image": img_path + "veg_breakfast.png", "details": "Slow-releasing energy."},
                "lunch": {"item": ("Pav with Sprouted Moong" if is_veg else "Egg Bhurji"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_breakfast.png"), "details": "High bioavailability protein."},
                "dinner": {"item": ("Paneer Tikka Masala" if is_veg else "Fish Tikka with Veggies"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Post-workout recovery champion."}
            },
            "wednesday": {
                "breakfast": {"item": "Kuttu ki Roti with Curd", "image": img_path + "veg_breakfast.png", "details": "Mineral-rich muscle fuel."},
                "lunch": {"item": ("Soya Chunks Pulao" if is_veg else "Chicken Kofta Curry & Rice"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Clean bulk essentials."},
                "dinner": {"item": ("Soya Chunks Curry with Rice" if is_veg else "Chicken Curry"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Dense nutrition for elite performance."}
            },
            "thursday": {
                "breakfast": {"item": ("High Protein Sattu Shake" if is_veg else "Boiled Eggs and Chicken Sausages"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Anabolic morning surge."},
                "lunch": {"item": ("Chole with Whole Wheat Roti" if is_veg else "Chicken Tikka Roll"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Micro and macro balanced meals."},
                "dinner": {"item": ("Paneer Curry with Millets" if is_veg else "Chicken Keema Paratha"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Sustained overnight amino release."}
            },
            "friday": {
                "breakfast": {"item": "Mango Lassi with Whey", "image": img_path + "veg_breakfast.png", "details": "Fast absorbing pre-workout fuel."},
                "lunch": {"item": ("Sweet Potato & Chole Chaat" if is_veg else "Fish Fry with Mashed Potatoes"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "High intensity carb loading."},
                "dinner": {"item": ("Kadhai Paneer with Veggies" if is_veg else "Chicken Roast with Veggies"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Growth hormone optimization meal."}
            },
            "saturday": {
                "breakfast": {"item": ("Paneer Bhurji with Toast" if is_veg else "Omelette with Cheese"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Solid whole-food breakfast."},
                "lunch": {"item": ("Soya Keema Matar" if is_veg else "Chicken Pasta Casserole"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Recovery phase caloric load."},
                "dinner": {"item": ("Paneer Tikka" if is_veg else "Grilled Fish Steaks"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Clean protein finish."}
            },
            "sunday": {
                "breakfast": {"item": "Badam Milk with Sabza", "image": img_path + "veg_breakfast.png", "details": "Restorative morning meal."},
                "lunch": {"item": ("Dal Makhani with Missi Roti" if is_veg else "Chicken & Sweet Corn Soup"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Comfort food for rest days."},
                "dinner": {"item": ("Tamatar Dhaniya Shorba" if is_veg else "Light Fish Stew"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Light ending to building week."}
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
    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
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
