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
        ('cat', OneHotEncoder(), categorical_cols)
    ])

# Function to make a prediction
def make_prediction(input_data):
    # Convert input data into DataFrame
    df = pd.DataFrame([input_data])

    # Convert 'Login Timestamp' to the format expected by the model
    df['Login Timestamp'] = pd.to_datetime(df['Login Timestamp'])
    df['Login Timestamp'] = df['Login Timestamp'].map(lambda x: (x - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s'))

    # Preprocess the input data
    X_transformed = preprocessor.transform(df)  # Use transform, not fit_transform

    # Make prediction
    prediction = model.predict(X_transformed)
    return "bot" if np.argmax(prediction) == 1 else "human"
