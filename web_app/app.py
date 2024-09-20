from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
with open('../ml_model/plant_watering_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    soil_moisture = data['soil_moisture']
    temperature = data['temperature']
    humidity = data['humidity']

    # Predict using the loaded model
    input_features = [[soil_moisture, temperature, humidity]]
    prediction = model.predict(input_features)[0]
    
    return jsonify({'needs_watering': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
