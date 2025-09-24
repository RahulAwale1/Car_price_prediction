# 🚗 Car Price Prediction API  

This repository demonstrates a complete **Machine Learning workflow** for predicting car prices, 
followed by an extension project where the trained model is deployed as a **REST API** using **FastAPI** 
and containerized with **Docker**.

---

## 📌 Features
- 🔹 Data preprocessing and ML model training using **scikit-learn**  
- 🔹 Model evaluation and selection of the best algorithm  
- 🔹 Model saved with **joblib** for inference  
- 🔹 **FastAPI REST API** for serving predictions (interactive Swagger docs at `/docs`)  
- 🔹 Containerized with **Docker** for deployment  

---

## 🛠 Tech Stack
- **Python 3.11+**  
- **FastAPI**  
- **scikit-learn, pandas, joblib**  
- **Docker**  

---

## 📂 Project Structure
```
Car Price Prediction/
 ├── app.py                    # REST API (FastAPI)
 ├── Car_price_prediction.ipynb # Original ML workflow notebook
 ├── CarPrice_Assignment.csv    # Dataset
 ├── columns.pkl                # Saved feature columns
 ├── Dockerfile                 # Container setup
 ├── model.pkl                  # Trained ML model
 ├── model.py                   # Inference logic (loads model, preprocesses input)
 ├── README.md                  # Project documentation
 ├── requirements.txt           # Dependencies
 └── train.py                   # Train model & save artifacts

```

---

## 🚀 Getting Started

### 1. Clone Repo
```bash
git clone https://github.com/RahulAwale1/Car_price_prediction.git
cd Car_price_prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train Model
```bash
python train.py
```
This will generate `model.pkl` and `columns.pkl`.

### 4. Run API (Locally)
```bash
uvicorn app:app --reload
```
Visit:
- Root: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
- Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

---

## 📡 API Usage

### ✅ Single Prediction
**POST** `/predict`

**Request JSON:**
```json
{
  "symboling": 1,
  "wheelbase": 100.0,
  "carwidth": 64.1,
  "curbweight": 2500,
  "horsepower": 120,
  "citympg": 25,
  "highwaympg": 30,
  "fueltype": "gas",
  "aspiration": "std",
  "carbody": "sedan"
}
```

**Response:**
```json
{
  "predicted_price": 18123.45
}
```

---

## 🐳 Docker Deployment

### 1. Build Image
```bash
docker build -t carprice-api .
```

### 2. Run Container
```bash
docker run -p 8000:8000 carprice-api
```

Now open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  


---

## 🚀 Next Steps (Future Enhancements)
- Add **batch prediction** endpoint (handle multiple cars at once)  
- Deploy to **Render / Railway / AWS** for a live public API  
- Add **CI/CD pipeline** for automated testing and deployment  

