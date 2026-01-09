# Low Level Design (LLD)

## 1. Data Input Module
Reads CSV file using pandas.read_csv().

## 2. Cleaning Module
- Replace infinite values with NaN
- Drop missing rows

## 3. Feature Engineering Module
- Daily returns calculation
- Rolling volatility (window=10)
- Moving average
- Liquidity ratio

## 4. Model Training Module
- Train-test split (80-20)
- RandomForestRegressor model
- Fit model on training data

## 5. Evaluation Module
- Mean Absolute Error
- Root Mean Squared Error
- R² Score

## 6. Prediction Module
- Accepts user inputs
- Returns volatility prediction

## 7. Error Handling
- File path validation
- NaN cleaning
- Version compatibility fixes
