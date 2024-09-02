import os
from tensorflow.keras.models import load_model
import numpy as np

# Load your model
model_path = os.path.join(os.path.dirname(__file__), '/Users/kaushalkento/Desktop/GroupProject./CAPTCHARefinement./project-root/models/trained_model3.h5')
model = load_model(model_path)

# Compile the model (add your optimizer, loss function, and metrics)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Example function for making predictions
def predict_user_behavior(data):
    # Preprocess the data to match the input format of the model
    input_data = np.array(data).reshape(1, -1)  # Assuming data is a 1D array

    # Make a prediction
    prediction = model.predict(input_data)
    return prediction
