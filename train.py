import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv("CarPrice_Assignment.csv")

df["brand"] = df["CarName"].apply(lambda x: x.split(" ")[0].lower())

df["brand"] = df["brand"].replace({
    "maxda": "mazda",
    "porcshce": "porsche",
    "toyouta": "toyota",
    "vokswagen": "volkswagen",
    "vw": "volkswagen"
})

selected_features = [
    "symboling", "fueltype", "aspiration", "carbody", "drivewheel",
    "enginesize", "horsepower", "curbweight", "citympg", "highwaympg", "brand"
]

X = df[selected_features]
y = df["price"]

categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
numeric_cols = X.select_dtypes(exclude=["object"]).columns.tolist()

numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_cols),
        ("cat", categorical_transformer, categorical_cols)
    ]
)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(n_estimators=100, random_state=60))
])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=60)

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "car_price_pipeline.pkl")

print("✅ Model trained and saved as car_price_pipeline.pkl")