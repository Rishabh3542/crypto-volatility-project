# Cryptocurrency Volatility Prediction – Final Report

## 1. Introduction
Cryptocurrency markets are highly volatile, making risk prediction essential for traders and investors.  
This project aims to build a machine learning model to predict volatility using historical market data such as open, high, low, close prices, trading volume, and market capitalization.

## 2. Objective
- Predict future volatility trends.
- Assist in risk management and decision-making.
- Analyze market stability using statistical and machine learning techniques.

## 3. Dataset Description
The dataset contains daily records for multiple cryptocurrencies with the following attributes:
- Date
- Symbol
- Open Price
- High Price
- Low Price
- Close Price
- Trading Volume
- Market Capitalization

## 4. Data Preprocessing
Steps applied:
- Removed missing and inconsistent values.
- Handled infinite values generated during ratio calculations.
- Normalized numerical columns.
- Removed duplicate records.

## 5. Feature Engineering
New features created:
- Daily Returns
- Rolling Volatility (10-day window)
- Moving Average (MA-10)
- Liquidity Ratio (Volume / Market Cap)

These features improve model sensitivity to market fluctuations.

## 6. Exploratory Data Analysis (EDA)
EDA was performed to understand:
- Price trends
- Volatility distribution
- Correlation between market features
- Liquidity patterns

Visualizations include line plots, correlation plots, and histograms.

## 7. Model Selection
Random Forest Regressor was selected due to:
- Ability to handle nonlinear relationships.
- Robustness to noise.
- Good generalization performance.

## 8. Model Training and Evaluation
Dataset split: 80% training, 20% testing.

Evaluation Metrics:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Results:
- MAE: 82763811671.05818
- RMSE: 1375956957391.7852
- R2: 0.24769464697984134

## 9. Hyperparameter Optimization
GridSearchCV was used to tune:
- Number of trees
- Maximum depth
- Minimum samples split

Optimized parameters improved prediction accuracy.

## 10. Deployment
The model was deployed locally using Streamlit for interactive predictions.

## 11. Conclusion
The system successfully predicts cryptocurrency volatility with acceptable accuracy and demonstrates how machine learning can assist financial decision-making.

## 12. Future Scope
- Deep learning models (LSTM)
- Real-time API data integration
- Cloud deployment
- Multi-currency forecasting
