import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load your dataset (CSV file with soil moisture, temperature, humidity, and watering status)
# Make sure your CSV contains columns: 'soil_moisture', 'temperature', 'humidity', 'needs_watering'
data = pd.read_csv('plant_data.csv')

# Features (X) and target (y)
X = data[['soil_moisture', 'temperature', 'humidity']]
y = data['needs_watering']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree Classifier
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Save the trained model to a file for later use in the IoT application
with open('plant_watering_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as plant_watering_model.pkl")
