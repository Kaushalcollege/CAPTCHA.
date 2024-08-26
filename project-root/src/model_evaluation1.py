import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical

# Load the trained model
model_path = '/Users/kaushalkento/Desktop/GroupProject./CAPTCHARefinement./project-root/models/trained_model1.h5'
model = load_model(model_path)

# Load the processed test data
file_path = '/Users/kaushalkento/Desktop/GroupProject./CAPTCHARefinement./project-root/data/processed1_rba-dataset.csv'
data = pd.read_csv(file_path)

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

# Fit and transform the test data
X_transformed = preprocessor.fit_transform(X)

# Convert target variable to categorical if needed
y_true = to_categorical(y)

# Make predictions
y_pred_prob = model.predict(X_transformed)
y_pred = (y_pred_prob > 0.5).astype(int)

# Evaluate the model
report = classification_report(y_true.argmax(axis=1), y_pred.argmax(axis=1))
matrix = confusion_matrix(y_true.argmax(axis=1), y_pred.argmax(axis=1))

# Print the evaluation results
print("Classification Report:\n", report)
print("Confusion Matrix:\n", matrix)

# Save the evaluation results
evaluation_report_path = '/Users/kaushalkento/Desktop/GroupProject./CAPTCHARefinement./project-root/reports/model_evaluation1_report.txt'
with open(evaluation_report_path, 'w') as f:
    f.write("Classification Report:\n")
    f.write(report)
    f.write("\nConfusion Matrix:\n")
    f.write(str(matrix))
