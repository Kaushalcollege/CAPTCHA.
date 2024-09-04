import os
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), '/Users/kaushalkento/Desktop/GroupProject./CAPTCHARefinement./project-root/models/trained_model6.keras')
model = tf.keras.models.load_model(model_path)

# Recompile the model to avoid issues with the optimizer state
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Define the preprocessing pipeline
categorical_cols = ['Country', 'Browser Name and Version', 'OS Name and Version']
numerical_cols = ['Round-Trip Time [ms]', 'Login Timestamp', 'Login Successful']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

# Function to make a prediction
def make_prediction(input_data):
    # Convert input data into DataFrame
    df = pd.DataFrame([input_data])

    # Ensure 'Login Timestamp' is converted to a numeric format expected by the model
    if 'Login Timestamp' in df.columns:
        df['Login Timestamp'] = pd.to_datetime(df['Login Timestamp'])
        df['Login Timestamp'] = df['Login Timestamp'].map(lambda x: (x - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s'))

    # Ensure all necessary columns are present
    missing_cols = [col for col in categorical_cols + numerical_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in input data: {missing_cols}")

    # Preprocess the input data
    X_transformed = preprocessor.transform(df)

    # Make prediction
    prediction = model.predict(X_transformed)

    # Return a JSON-serializable result
    return "bot" if np.argmax(prediction) == 1 else "human"
