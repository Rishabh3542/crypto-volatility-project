# 🚀 Cryptocurrency Volatility Prediction

A machine learning project to predict cryptocurrency market volatility using historical OHLC prices, volume, and market capitalization data.

---

## 📌 Project Objectives
- Predict cryptocurrency volatility trends.
- Improve risk assessment and trading strategies.
- Analyze market behavior through data visualization and ML modeling.

---

## 📂 Project Structure

crypto-volatility-project/
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│   ├── 1_eda.ipynb
│   ├── 2_feature_engineering.ipynb
│   ├── 3_model_training.ipynb
│   └── 4_hyperparameter_tuning.ipynb
│
├── app/
│   └── app.py
│
├── reports/
│   ├── EDA_Report_1.png
|   ├── EDA_Report.png
│   ├── HLD.md
│   ├── LLD.md
│   ├── Pipeline.md
│   └── Final_Report.md
│
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Installation

### 1. Clone Repository
git clone https://github.com/USERNAME/crypto-volatility-project.git
cd crypto-volatility-project

### 2. Create Virtual Environment
python -m venv venv

Activate:
Windows → venv\Scripts\activate  
Mac/Linux → source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

---

## ▶️ How to Run

### Run Notebooks
jupyter notebook

Open notebooks in order:
1_eda.ipynb  
2_feature_engineering.ipynb  
3_model_training.ipynb  
4_hyperparameter_tuning.ipynb  

---

### Run Streamlit App
streamlit run app/app.py

---

## 📊 Model
- Algorithm: Random Forest Regressor
- Input Features: Moving Average, Liquidity, Volume
- Target: Volatility

---

## 📈 Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 🧪 Future Improvements
- Deep learning models
- Live market data integration
- Cloud deployment
- Automated pipelines

---

## 👨‍💻 Author
Rishabh
