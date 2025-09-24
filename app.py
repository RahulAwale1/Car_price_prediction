from fastapi import FastAPI
from pydantic import BaseModel
import model

app = FastAPI(title="Car Price Prediction API")

# Define input schema (minimal example – add more fields as needed)
class CarFeatures(BaseModel):
    CarName: str
    symboling: int
    wheelbase: float
    carwidth: float
    curbweight: int
    horsepower: int
    citympg: int
    highwaympg: int
    fueltype: str
    aspiration: str
    carbody: str
    drivewheel: str
    enginesize: int

@app.get("/")
def root():
    return {"message": "Car Price Prediction API is running 🚗💰"}

@app.post("/predict")
def predict_price(features: CarFeatures):
    input_dict = features.dict()
    price = model.predict(input_dict)
    return {"predicted_price": round(price, 2)}
