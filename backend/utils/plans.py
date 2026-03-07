def get_diet_plan_details(plan_id, diet_type='non_vegetarian'):
    is_veg = diet_type == 'vegetarian'
    img_path = "/assets/img/"
    
    plans = {
        1: {
            "name": "Fat Loss & Metabolic Reset",
            "desc": "High thermic effect diet designed for sustainable fat loss while maintaining muscle.",
            "macros": {"protein": 40, "carbs": 25, "fats": 35},
            "monday": {
                "breakfast": {"item": ("Poha with Sprouts" if is_veg else "Avocado Egg Toast"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Rich in complex carbs to start your day."},
                "lunch": {"item": "Brown Rice & Dal", "image": img_path + "veg_main.png", "details": "Fiber-rich meal with complete plant proteins."},
                "dinner": {"item": ("Grilled Paneer" if is_veg else "Grilled Chicken"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "High protein, low carb for recovery."}
            },
            "tuesday": {
                "breakfast": {"item": ("Paneer Scramble" if is_veg else "Boiled Eggs"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Quick high-protein start."},
                "lunch": {"item": ("Soya Curry" if is_veg else "Tuna Salad"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Lean protein for afternoon energy."},
                "dinner": {"item": ("Tofu Stir-fry" if is_veg else "Pan-seared Salmon"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Omega-3 rich for inflammation control."}
            },
            "wednesday": {
                "breakfast": {"item": "Oats with Nuts & Apple", "image": img_path + "veg_breakfast.png", "details": "Slow-release carbs for steady energy."},
                "lunch": {"item": ("Chickpea Salad" if is_veg else "Grilled Chicken Wraps"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "High fiber and protein lunch."},
                "dinner": {"item": ("Lentil Soup" if is_veg else "Roasted Turkey"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Light and easy to digest."}
            },
            "thursday": {
                "breakfast": {"item": ("Besan Chilla" if is_veg else "Omelette with Toast"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Traditional protein-rich breakfast."},
                "lunch": {"item": ("Bajra Khichdi" if is_veg else "Quinoa Chicken Bowl"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Nutrient-dense ancient grains."},
                "dinner": {"item": ("Mix Veg Curry" if is_veg else "Baked Fish"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Micronutrient-rich evening meal."}
            },
            "friday": {
                "breakfast": {"item": "Fruit & Greek Yogurt Bowl", "image": img_path + "veg_breakfast.png", "details": "Probiotic-rich refreshing start."},
                "lunch": {"item": ("Paneer Salad" if is_veg else "Turkey Breast Salad"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Low calorie, high satiety."},
                "dinner": {"item": ("Roasted Tofu & Broccoli" if is_veg else "Grilled Shrimp"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Metabolism boosting light dinner."}
            },
            "saturday": {
                "breakfast": {"item": ("Moong Dal Chilla" if is_veg else "Scrambled Eggs on Rye"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Complex carb loaded breakfast."},
                "lunch": {"item": ("Veggie Sushi (Avocado)" if is_veg else "Sashimi / Salmon Poke"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Clean fats and quality protein."},
                "dinner": {"item": ("Cottage Cheese Steak" if is_veg else "Lean Beef Tagine"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Muscle repair focusing meal."}
            },
            "sunday": {
                "breakfast": {"item": "Sundays Healthy Pancake with Berries", "image": img_path + "veg_breakfast.png", "details": "Weekend treat without the guilt."},
                "lunch": {"item": "Hearty Vegetable Stew", "image": img_path + "veg_main.png", "details": "Vitamin-packed weekend lunch."},
                "dinner": {"item": ("Minestrone Soup" if is_veg else "Light Chicken Broth"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Detoxifying and light dinner."}
            }
        },
        2: {
            "name": "Balanced Maintenance",
            "desc": "Optimal macronutrient balance for stable energy and weight maintenance.",
            "monday": {
                "breakfast": {"item": ("Paneer Paratha" if is_veg else "Eggs & Moong Dal Chilla"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Balanced protein and energy bowl."},
                "lunch": {"item": "Chapati & Veg Curry", "image": img_path + "veg_main.png", "details": "Standard balanced energy lunch."},
                "dinner": {"item": ("Mix Veg Khichdi" if is_veg else "Fish Curry & Rice"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Easily digestible for sleep."}
            },
            "tuesday": {
                "breakfast": {"item": "Berry & Nut Smoothie", "image": img_path + "veg_breakfast.png", "details": "Antioxidant-rich quick meal."},
                "lunch": {"item": ("Paneer Tikki" if is_veg else "Chicken Caesar Salad"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Light yet protein dense."},
                "dinner": {"item": "Vegetable Soup", "image": img_path + "veg_main.png", "details": "Prevents late-night cravings."}
            },
            "wednesday": {
                "breakfast": {"item": ("Sprouted Moong Salad" if is_veg else "Egg White Omelette"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Enzyme-rich morning start."},
                "lunch": {"item": "Quinoa & Mix Bean Salad", "image": img_path + "veg_main.png", "details": "High protein plant-based lunch."},
                "dinner": {"item": ("Tofu & Bell Pepper Stir-fry" if is_veg else "Grilled Chicken Breast"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Balanced recovery meal."}
            },
            "thursday": {
                "breakfast": {"item": ("Ragi Malt" if is_veg else "Greek Yogurt with Granola"), "image": img_path + "veg_breakfast.png", "details": "Calcium-rich morning fuel."},
                "lunch": {"item": ("Brown Rice & Kadhi" if is_veg else "Lemon Chicken with Couscous"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Probiotic-rich and energizing."},
                "dinner": {"item": ("Baked Sweet Potato & Beans" if is_veg else "Roast Salmon & Asparagus"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Fiber and Omega-3 balance."}
            },
            "friday": {
                "breakfast": {"item": "Chia Seed Pudding", "image": img_path + "veg_breakfast.png", "details": "Hydration and fiber focus."},
                "lunch": {"item": ("Paneer Bhurji with Rotis" if is_veg else "Mackerel with Steamed Veggies"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Satisfying protein-rich lunch."},
                "dinner": {"item": ("Vegetable Lasagna (Healthy)" if is_veg else "Chicken Stew"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Comforting yet clean dinner."}
            },
            "saturday": {
                "breakfast": {"item": ("Vegetable Upma" if is_veg else "Shakshuka Eggs"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Slow energy release for the weekend."},
                "lunch": {"item": "Rainbow Salad with Toasted Seeds", "image": img_path + "veg_main.png", "details": "Vitamin and micronutrient load."},
                "dinner": {"item": ("Mushroom Risotto (Healthy)" if is_veg else "Grilled Pork Chops"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Rich in flavor, clean in macros."}
            },
            "sunday": {
                "breakfast": {"item": "Oatmeal with Honey & Banana", "image": img_path + "veg_breakfast.png", "details": "The classic weekend morning."},
                "lunch": {"item": "Paneer & Spinach Wraps", "image": img_path + "veg_main.png", "details": "Portable and nutrient-dense."},
                "dinner": {"item": "Clear Vegetable Broth", "image": img_path + "veg_main.png", "details": "Light finish to the week."}
            }
        },
        3: {
            "name": "Muscle Building & Strength",
            "desc": "Caloric surplus with high protein and clean carbs to fuel muscle hypertrophy.",
            "monday": {
                "breakfast": {"item": "Peanut Butter & Banana Toast", "image": img_path + "veg_breakfast.png", "details": "Power-packed for training days."},
                "lunch": {"item": ("Paneer Butter Masala" if is_veg else "Chicken & Sweet Potato"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Muscle glycogen refueling."},
                "dinner": {"item": ("Lentil Burger" if is_veg else "Beef Mince & Pasta"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "High protein load for overnight synthesis."}
            },
            "tuesday": {
                "breakfast": {"item": "Oats with Walnuts & Honey", "image": img_path + "veg_breakfast.png", "details": "Slow-releasing energy."},
                "lunch": {"item": ("Pav with Sprouted Moong" if is_veg else "Egg Bhurji"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_breakfast.png"), "details": "High bioavailability protein."},
                "dinner": {"item": ("Paneer Steaks" if is_veg else "Grilled Fish & Broccoli"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Post-workout recovery champion."}
            },
            "wednesday": {
                "breakfast": {"item": "Buckwheat Pancakes with Nuts", "image": img_path + "veg_breakfast.png", "details": "Mineral-rich muscle fuel."},
                "lunch": {"item": ("Soy Nuggets with Brown Rice" if is_veg else "Turkey Meatballs & Rice"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Clean bulk essentials."},
                "dinner": {"item": ("Baked Tofu with Soba Noodles" if is_veg else "Ribeye Steak with Roast Roots"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Dense nutrition for elite performance."}
            },
            "thursday": {
                "breakfast": {"item": ("Protein Oatmeal" if is_veg else "Bacon & Eggs (Lean)"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Anabolic morning surge."},
                "lunch": {"item": ("Hummus & Whole Wheat Pita" if is_veg else "Grilled Chicken Tacos"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Micro and macro balanced meals."},
                "dinner": {"item": ("Paneer Curry with Quinoa" if is_veg else "Ground Beef Tacos"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Sustained overnight amino release."}
            },
            "friday": {
                "breakfast": {"item": "Smoothie Bowl with Protein Powder", "image": img_path + "veg_breakfast.png", "details": "Fast absorbing pre-workout fuel."},
                "lunch": {"item": ("Sweet Potato & Chickpea Salad" if is_veg else "Tuna Steaks with Mash"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "High intensity carb loading."},
                "dinner": {"item": ("Vegetable Stir-fry + Extra Paneer" if is_veg else "Lamb Chops & Veggies"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Growth hormone optimization meal."}
            },
            "saturday": {
                "breakfast": {"item": ("Tofu Scramble with Toast" if is_veg else "Omelette with Cheese"), "image": img_path + ("veg_breakfast.png" if is_veg else "non_veg_breakfast.png"), "details": "Solid whole-food breakfast."},
                "lunch": {"item": ("Veggie Shepherd's Pie" if is_veg else "Hearty Ground Turkey Pasta"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Recovery phase caloric load."},
                "dinner": {"item": ("Paneer Shashlik" if is_veg else "Grilled Salmon Steaks"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Clean protein finish."}
            },
            "sunday": {
                "breakfast": {"item": "Mixed Berry Chia Pudding", "image": img_path + "veg_breakfast.png", "details": "Restorative morning meal."},
                "lunch": {"item": ("Whole Wheat Pasta with Lentils" if is_veg else "Chicken & Corn Stew"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Comfort food for rest days."},
                "dinner": {"item": ("Tomato & Basil Soup (High Protein)" if is_veg else "Clear Fish Broth"), "image": img_path + ("veg_main.png" if is_veg else "non_veg_main.png"), "details": "Light ending to building week."}
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
