from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    gender = int(request.form['gender'])
    vip = int(request.form['vip'])
    income = float(request.form['income'])
    children = int(request.form['children'])
    age = int(request.form['age'])
    attractiveness = int(request.form['attractiveness'])
    
    # Create the input array for prediction
    input_data = np.array([[gender, vip, income, children, age, attractiveness]])
    
    # Scale the input data
    input_data_scaled = scaler.transform(input_data)
    
    # Perform the prediction
    predicted_matches = model.predict(input_data_scaled)[0]

    return f'<h1>Predicted Matches: {predicted_matches}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
