# 🚗 Car Price Prediction – From Machine Learning to Deployment  

This project predicts **car prices** using the **Car Price Assignment dataset**.  
It demonstrates a complete workflow:  
- Exploratory Data Analysis & Model Training in Jupyter Notebook  
- Feature Engineering for business insights  
- Model deployment as a **REST API** using **FastAPI**  
- Containerization with **Docker**  

---

## 📊 Part 1: Machine Learning Workflow (Notebook)

### 📌 Project Overview
- **Type:** Supervised Learning (Regression)  
- **Problem:** Predict the continuous variable `price`  
- **Dataset:** Car Price Assignment Dataset (205 entries, 26 columns)  
- **Target Variable:** `price`  

### 🔧 Feature Engineering
- **brand** → extracted from `CarName`  
- **luxury flag** → marks premium brands (BMW, Audi, Mercedes, Jaguar, Porsche)  
- **fixed typos** in brand names (`vw` → Volkswagen, `vokswagen` → Volkswagen, `maxda` → Mazda, etc.)  
- Removed **irrelevant column**: `car_ID`  

### 🛠️ Steps
1. **Data Cleaning & Preparation**  
   - Dropped unused columns  
   - Encoded categorical features using Label Encoding  
2. **Feature Engineering**  
   - Added `brand` and `luxury` features  
   - Corrected brand typos  
3. **Model Training**  
   - Linear Regression, Ridge, Lasso  
   - Decision Tree, Random Forest  
4. **Evaluation Metrics**  
   - MAE, RMSE, R² Score  
5. **Results Visualization**  
   - Compared model performance  

### 📌 Results
| Model              | MAE ↓   | RMSE ↓   | R² ↑   |
|--------------------|---------|----------|--------|
| Linear Regression  | 1992.09 | 2603.75  | 0.853  |
| Ridge Regression   | 1982.39 | 2600.44  | 0.854  |
| Lasso Regression   | 1992.11 | 2603.78  | 0.853  |
| Decision Tree      | 1559.32 | 2135.54  | 0.901  |
| Random Forest      | **1393.35** | **2068.17** | **0.908** |

**Key Insight:** Random Forest gave the best performance, capturing non-linear feature interactions and reducing prediction error significantly compared to linear models. 

### 🚀 Tools & Libraries
- Python  
- Pandas, NumPy – data handling  
- Matplotlib – visualization  
- Scikit-learn – regression models & evaluation  

---

## 📦 Part 2: Deployment as API

After selecting the **Random Forest model**, the project was extended into deployment:  

### 📌 Features
- End-to-end ML pipeline with preprocessing + Random Forest  
- Feature engineering integrated (brand extraction + cleaning)  
- REST API built with FastAPI  
- Containerized with Docker for deployment  

### 🛠 Tech Stack
- **Python 3.11+**  
- **scikit-learn, pandas, joblib**  
- **FastAPI + Uvicorn**  
- **Docker**  

### 📂 Project Structure
```
Car Price Prediction/
 ├── app.py                  # FastAPI app (API server)
 ├── Car_price_prediction.ipynb # Original ML workflow notebook
 ├── model.py                # Inference logic (pipeline + brand cleaning)
 ├── train.py                # Train pipeline and save as .pkl
 ├── car_price_pipeline.pkl  # Saved ML pipeline
 ├── CarPrice_Assignment.csv # Dataset
 ├── requirements.txt        # Python dependencies
 ├── Dockerfile              # Container setup
 ├── Car_price_prediction.ipynb # Original ML workflow notebook
 └── README.md               # Documentation
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
This generates `car_price_pipeline.pkl`.

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
  "CarName": "toyouta corolla",
  "symboling": 1,
  "wheelbase": 97.0,
  "carwidth": 64.0,
  "curbweight": 2500,
  "horsepower": 120,
  "citympg": 25,
  "highwaympg": 30,
  "fueltype": "gas",
  "aspiration": "std",
  "carbody": "sedan",
  "drivewheel": "fwd",
  "enginesize": 130
}
```

**Response:**
```json
{
  "predicted_price": 18234.56
}
```

👉 Note: `CarName` is auto-corrected (e.g., `"toyouta"` → `"toyota"`, `"vw"` → `"volkswagen"`).

---

## 🐳 Docker Deployment

### 1. Train Pipeline (before build)
```bash
python train.py
```

### 2. Build Image
```bash
docker build -t carprice-api .
```

### 3. Run Container
```bash
docker run -p 8000:8000 carprice-api
```

Now open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 Resume Highlight
> **Car Price Prediction – ML to Deployment**  
> - Built an end-to-end ML workflow (EDA, feature engineering, regression models).  
> - Selected Random Forest as best model (R² = 0.908).  
> - Deployed the model as a REST API with FastAPI and Docker.  
> - Demonstrated complete ML lifecycle: from **exploration in Jupyter Notebook** to **production-ready microservice**.  
