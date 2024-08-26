# src/model_evaluation.py

from tensorflow.keras.models import load_model
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load the model
model = load_model('../models/trained_model.h5')

# Print model summary to get input shape
print("Model summary:")
model.summary()

# Load the test data
data = pd.read_csv('../data/processed1_rba-dataset.csv')

# Print dataset columns to verify
print("Dataset columns:", data.columns)

# Convert timestamps to numeric features (adjust based on your specific needs)
data['Login Timestamp'] = pd.to_datetime(data['Login Timestamp'])
data['Login Timestamp'] = data['Login Timestamp'].map(lambda x: (x - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s'))

# Define the list of columns used for training (must match the training feature set)
# Update this list based on the actual columns in your dataset
required_columns = ['Round-Trip Time [ms]', 'Country', 'Region', 'City', 'ASN', 'Device Type', 'Login Successful']

# Ensure that all required columns are in the DataFrame
missing_columns = [col for col in required_columns if col not in data.columns]
if missing_columns:
    raise ValueError(f"Missing columns in the dataset: {missing_columns}")

# Select the required columns
X_test = data[required_columns]

# Convert to numeric and handle missing values
X_test = X_test.apply(pd.to_numeric, errors='coerce').fillna(0)

# Print the shape of X_test to match the model's input
print("Shape of X_test:", X_test.shape)

# Example target
y_test = data['Is Account Takeover']

# Scale features consistently with training data
scaler = StandardScaler()
# Assuming the scaler used during training was fitted on the same features
X_test_scaled = scaler.fit_transform(X_test)

# Print the shape of scaled data to ensure it matches model input
print("Shape of X_test_scaled:", X_test_scaled.shape)

# Make predictions
try:
    predictions = model.predict(X_test_scaled)
    predictions = (predictions > 0.5).astype(int)

    # Evaluate the model
    report = classification_report(y_test, predictions)
    matrix = confusion_matrix(y_test, predictions)

    # Save the evaluation results
    with open('../reports/model_evaluation_report.txt', 'w') as f:
        f.write("Classification Report:\n")
        f.write(report)
        f.write("\nConfusion Matrix:\n")
        f.write(str(matrix))

except Exception as e:
    print("An error occurred during prediction:", e)
