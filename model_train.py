
import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model():
    """
    Loads the Iris dataset, trains a Random Forest model, and saves it.
    """
    print("Loading Iris dataset...")
    # 1. Load the dataset
    data = load_iris()
    X = data.data
    y = data.target
    feature_names = data.feature_names
    target_names = data.target_names

    # 2. Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Initialize and train the model
    print(f"Training RandomForestClassifier on {len(X_train)} samples...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 4. Evaluate the model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Training Complete. Accuracy: {accuracy:.4f}")

    # 5. Save the model and metadata
    model_data = {
        'model': model,
        'target_names': target_names,
        'feature_names': feature_names
    }
    joblib.dump(model_data, 'model.pkl')
    print("Model saved to model.pkl")

if __name__ == "__main__":
    train_model()
