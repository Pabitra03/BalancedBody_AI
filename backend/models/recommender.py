import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

class RecommendationModel:
    def __init__(self):
        self.dt_diet = None
        self.dt_workout = None
        self._train_models()

    def _train_models(self):
        # Synthetic dataset for recommendations (for the scope of this project)
        # Features: Age, Weight, Height, ActivityLevel(1-5), Goal(0:loss, 1:maintain, 2:gain)
        data = {
            'age': [25, 30, 22, 40, 35, 28, 45, 20, 50, 27],
            'weight': [85, 70, 60, 95, 75, 80, 100, 55, 90, 65],
            'height': [175, 180, 160, 185, 170, 178, 175, 165, 180, 168],
            'activity_level': [2, 4, 3, 1, 5, 2, 1, 4, 2, 3],
            'goal': [0, 1, 2, 0, 1, 0, 0, 2, 0, 1],
            'diet_plan': [1, 2, 3, 1, 2, 1, 1, 3, 1, 2], # 1: Low Carb, 2: Balanced, 3: High Protein/Carb
            'workout_plan': [1, 3, 2, 1, 3, 1, 1, 2, 1, 2] # 1: Cardio/HIIT, 2: Strength, 3: Complete Athlete
        }
        df = pd.DataFrame(data)
        
        X = df[['age', 'weight', 'height', 'activity_level', 'goal']]
        y_diet = df['diet_plan']
        y_workout = df['workout_plan']
        
        self.dt_diet = DecisionTreeClassifier()
        self.dt_workout = DecisionTreeClassifier()
        
        self.dt_diet.fit(X, y_diet)
        self.dt_workout.fit(X, y_workout)

    def predict(self, age, weight, height, activity_level_str, goal_str):
        activity_level_map = {
             'sedentary': 1, 'lightly_active': 2, 'moderately_active': 3, 'very_active': 4, 'super_active': 5
        }
        goal_map = {'loss': 0, 'maintain': 1, 'gain': 2}
        
        act_val = activity_level_map.get(activity_level_str, 1)
        goal_val = goal_map.get(goal_str, 1)
        
        X_pred = np.array([[age, weight, height, act_val, goal_val]])
        
        try:
            diet_plan_id = int(self.dt_diet.predict(X_pred)[0])
            workout_plan_id = int(self.dt_workout.predict(X_pred)[0])
            return diet_plan_id, workout_plan_id
        except Exception as e:
            print(f"Prediction error: {e}")
            return 2, 2 # Default fallback
            
# Create a singleton instance
recommender = RecommendationModel()
