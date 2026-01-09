# High Level Design (HLD)
Project Title: Cryptocurrency Volatility Prediction

## 1. Objective
To predict cryptocurrency volatility using historical OHLC, volume, and market capitalization data.

## 2. System Architecture
User → Dataset → Preprocessing → Feature Engineering → ML Model → Evaluation → Prediction Output

## 3. Components
1. Data Layer
   - Input CSV dataset
   - Stores OHLC, volume, market cap

2. Processing Layer
   - Missing value handling
   - Scaling & normalization
   - Feature generation

3. Machine Learning Layer
   - Random Forest Regressor
   - Model training and prediction

4. Evaluation Layer
   - MAE
   - RMSE
   - R² Score

5. Deployment Layer
   - Streamlit web interface

## 4. Technology Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Matplotlib

## 5. Output
- Volatility prediction
- Performance metrics
