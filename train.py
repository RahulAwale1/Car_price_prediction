import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("CarPrice_Assignment.csv")

X = df.drop(columns=["price"])
y = df["price"]

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=60)

model = RandomForestRegressor(n_estimators=100, random_state=60)
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
joblib.dump(list(X.columns), "columns.pkl")

print("✅ Model trained and saved as model.pkl")