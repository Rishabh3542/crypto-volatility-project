import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl","rb"))

st.title("Crypto Volatility Predictor")

ma = st.number_input("Moving Average")
liq = st.number_input("Liquidity")
vol = st.number_input("Volume")

if st.button("Predict"):
    x = np.array([[ma, liq, vol]])
    result = model.predict(x)
    st.write("Predicted Volatility:", result[0])
