import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Sample data (replace this with your actual dataset)
data = {
    'soil_moisture': [20, 30, 50, 60, 80, 90],
    'temperature': [20, 22, 25, 27, 30, 35],
    'humidity': [40, 50, 60, 70, 80, 90],
    'needs_watering': [0, 0, 1, 1, 1, 1]  # 0: No, 1: Yes
}

# Create a DataFrame
df = pd.DataFrame(data)

# Features and target variable
X = df[['soil_moisture', 'temperature', 'humidity']]
y = df['needs_watering']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Save the model to a file
joblib.dump(model, 'ml_model/plant_watering_model.pkl')
print("Model saved as plant_watering_model.pkl")
