import joblib
import pandas as pd

# Load artifacts
pipeline = joblib.load("car_price_pipeline.pkl")

def clean_brand(name: str) -> str:
    brand = name.split(" ")[0].lower()
    corrections = {
        "maxda": "mazda",
        "porcshce": "porsche",
        "toyouta": "toyota",
        "vokswagen": "volkswagen",
        "vw": "volkswagen"
    }
    return corrections.get(brand, brand)

def predict(input_dict: dict):
    """
    input_dict: dictionary of features for a single car
    returns: predicted price
    """
    # Convert dict → dataframe
    df = pd.DataFrame([input_dict])

    if "CarName" in df.columns:
        df["brand"] = df["CarName"].apply(clean_brand)
        df = df.drop(columns=["CarName"])

    prediction = pipeline.predict(df)[0]
    return float(prediction)
