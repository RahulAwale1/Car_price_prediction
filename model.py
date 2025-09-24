import joblib
import pandas as pd

# Load artifacts
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

def predict(input_dict: dict):
    """
    input_dict: dictionary of features for a single car
    returns: predicted price
    """
    # Convert dict → dataframe
    df = pd.DataFrame([input_dict])

    # Align columns (so API input matches training schema)
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)[0]
    return float(prediction)
