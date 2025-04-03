from flask import Flask, render_template, request
from fuzzy_logic import run_fuzzy_logic

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', result=False)

@app.route('/predict', methods=['POST'])
def predict():
    hunger = request.form['hunger']
    time = request.form['time']
    goal = request.form['goal']
    activity = request.form['activity']
    preference = request.form['preference']

    category, dish_name, image_path, tagline = run_fuzzy_logic(hunger, time, goal, activity, preference)

    return render_template('index.html', result=True, category=category, dish=dish_name, image=image_path, tagline=tagline)

if __name__ == '__main__':
    app.run(debug=True)