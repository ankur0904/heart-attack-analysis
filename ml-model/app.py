from flask import Flask, render_template, request
import numpy as np
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = {
        "exercise_time": int(request.form.get("exercise")),
        "gender": str(request.form.get("gender")).lower(),
        "is_smoker": str(request.form.get("smoker")).lower(),
        "age": int(request.form.get("age")),
        "bp": request.form.get("bp"),
        "is_diabetic": str(request.form.get("is_diabetic")).lower(),
        "family_heart_problem_background": str(request.form.get("family_heart_problem_background")).lower(),
        "health_status": str(request.form.get("health_status")).lower()
    }
    print(data)
    