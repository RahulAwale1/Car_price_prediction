# 🚗 Car Price Prediction with Machine Learning

This project predicts **car prices** using the **Car Price Assignment dataset**, applying multiple regression models and **feature engineering**. It demonstrates how machine learning can be applied in real-world business problems like car resale valuation.  

---

## 📊 Project Overview
- **Type:** Supervised Learning (Regression)  
- **Problem:** Predict the continuous variable `price`  
- **Dataset:** Car Price Assignment Dataset (205 entries, 26 columns)  
- **Target Variable:** `price`  

---

## 🔧 Feature Engineering
To improve model accuracy, additional features were created:
- **brand** → extracted from `CarName`  
- **luxury flag** → marks premium brands (BMW, Audi, Mercedes, Jaguar, Porsche)  
- **fixed typos** in brand names (`vw` → Volkswagen, `vokswagen` → Volkswagen, `maxda` → Mazda, etc.)  
- Removed **irrelevant column**: `car_ID`  

---

## 🛠️ Steps in the Project
1. **Data Cleaning & Preparation**  
   - Dropped unused columns  
   - Encoded categorical features using Label Encoding  
2. **Feature Engineering** (brand extraction, luxury flag, typo correction)  
3. **Model Training**  
   - Linear Regression  
   - Ridge Regression  
   - Lasso Regression  
   - Decision Tree  
   - Random Forest  
4. **Evaluation Metrics**  
   - MAE (Mean Absolute Error)  
   - RMSE (Root Mean Squared Error)  
   - R² Score (Goodness of Fit)  
5. **Results Visualization** (bar chart of R² across models)  

---

## 📌 Results
| Model              | MAE ↓   | RMSE ↓   | R² ↑   |
|--------------------|---------|----------|--------|
| Linear Regression  | 1992.09 | 2603.75  | 0.853  |
| Ridge Regression   | 1982.39 | 2600.44  | 0.854  |
| Lasso Regression   | 1992.11 | 2603.78  | 0.853  |
| Decision Tree      | 1559.32 | 2135.54  | 0.901  |
| Random Forest      | **1393.35** | **2068.17** | **0.908** |

**Key Insight:** Random Forest gave the best performance, capturing non-linear feature interactions and reducing prediction error significantly compared to linear models. 

---

## 🚀 Tools & Libraries
- **Python**  
- **Pandas, NumPy** – data handling  
- **Matplotlib** – visualization  
- **Scikit-learn** – regression models & evaluation  

---

