import pandas as pd
import pickle
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Define paths
_script_dir = os.path.dirname(os.path.abspath(__file__))
_project_root_approx = os.path.dirname(_script_dir)
_django_app_model_dir = os.path.join(_project_root_approx, 'project', 'app', 'ml_models')
PIPELINE_NAME = "pipeline_dt.pkl"
PIPELINE_PATH = os.path.join(_django_app_model_dir, PIPELINE_NAME)

def load_and_preprocess_data(file_path):
    """
    Load and preprocess the student exam data.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Preprocessed data.
    """
    # Load the data
    data = pd.read_csv(file_path)

    # Example preprocessing steps (customize as needed):
    # Drop rows with missing values
    data = data.dropna()

    # Convert categorical columns to numeric (if any)
    for column in data.select_dtypes(include=['object']).columns:
        data[column] = data[column].astype('category').cat.codes

    return data

def save_data_to_pickle(data, pickle_path):
    """
    Save the preprocessed data to a pickle file.

    Args:
        data (pd.DataFrame): The preprocessed data.
        pickle_path (str): Path to save the pickle file.
    """
    with open(pickle_path, 'wb') as file:
        pickle.dump(data, file)

def load_data_from_pickle(pickle_path):
    """
    Load data from a pickle file.

    Args:
        pickle_path (str): Path to the pickle file.

    Returns:
        pd.DataFrame: The loaded data.
    """
    with open(pickle_path, 'rb') as file:
        return pickle.load(file)

def train_and_save_pipeline(file_path):
    """
    Train a machine learning pipeline and save it to a file.

    Args:
        file_path (str): Path to the CSV file containing the dataset.
    """
    # Load dataset
    df = pd.read_csv(file_path)

    # Drop ID column if it exists
    if 'id' in df.columns:
        df.drop(columns=['id'], inplace=True)

    TARGET_COLUMN = 'exam_score'

    # Separate features and target
    X = df.drop(TARGET_COLUMN, axis=1)
    y = df[TARGET_COLUMN]

    # Identify categorical and numerical features
    categorical_features = X.select_dtypes(include='object').columns.tolist()
    numerical_features = X.select_dtypes(include=np.number).columns.tolist()

    # Create preprocessing pipelines for numerical and categorical features
    numerical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', MinMaxScaler())
    ])

    categorical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('encoder', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1))
    ])

    # Create preprocessor using ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_pipeline, categorical_features),
            ('num', numerical_pipeline, numerical_features)
        ],
        remainder='passthrough'
    )

    # Create the full machine learning pipeline
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model_pipeline.fit(X_train, y_train)

    # Evaluate
    y_pred = model_pipeline.predict(X_test)
    print("R2 Score:", r2_score(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))

    # Ensure the target directory for the pipeline exists
    os.makedirs(_django_app_model_dir, exist_ok=True)

    # Save the single pipeline object
    with open(PIPELINE_PATH, "wb") as f:
        pickle.dump(model_pipeline, f)
    print(f"Pipeline saved to {PIPELINE_PATH}")

# Example usage
if __name__ == "__main__":
    file_path = "data/student_exam_data_new.csv"
    pickle_path = "data/student_exam_data.pkl"

    # Load and preprocess the data
    processed_data = load_and_preprocess_data(file_path)

    # Save the data to a pickle file
    save_data_to_pickle(processed_data, pickle_path)
    print(f"Data saved to {pickle_path}")

    # Load the data back from the pickle file
    loaded_data = load_data_from_pickle(pickle_path)
    print("Loaded data:")
    print(loaded_data.head())

    # Train and save the machine learning pipeline
    train_and_save_pipeline(file_path)