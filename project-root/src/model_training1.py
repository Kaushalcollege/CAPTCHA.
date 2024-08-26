import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Load the processed data
file_path = '/Users/kaushalkento/Desktop/GroupProject./CAPTCHARefinement./project-root/data/processed1_rba-dataset.csv'
data = pd.read_csv(file_path)

# Print columns to verify
print("Available columns:", data.columns)

# Adjusted feature columns and target column
feature_columns = ['Round-Trip Time [ms]', 'Country', 'Browser Name and Version',
                   'OS Name and Version', 'Login Timestamp', 'Login Successful']

# Convert Login Timestamp to a numeric value
data['Login Timestamp'] = pd.to_datetime(data['Login Timestamp'])
data['Login Timestamp'] = data['Login Timestamp'].map(lambda x: (x - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s'))

# Extract features and target
X = data[feature_columns]
y = data['Is Attack IP']

# Identify categorical and numerical columns
categorical_cols = ['Country', 'Browser Name and Version', 'OS Name and Version']
numerical_cols = ['Round-Trip Time [ms]', 'Login Timestamp', 'Login Successful']

# Create a ColumnTransformer to handle both types of data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])

# Apply the transformations
X_transformed = preprocessor.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.3, random_state=42)

# Convert target variable to categorical if needed
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Define the neural network model
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(2, activation='softmax'))  # Assuming binary classification

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss}")
print(f"Test Accuracy: {accuracy}")

# Save the trained model in the Keras format
model_save_path = '/Users/kaushalkento/Desktop/GroupProject./CAPTCHARefinement./project-root/models/trained_model1.h5'
model.save(model_save_path)
