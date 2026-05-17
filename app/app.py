import streamlit as st
from predict import predict_score

st.title("Alternative Credit Scoring Platform")

transactions = st.number_input("Monthly Transactions")
savings = st.slider("Savings Score", 0.0, 1.0)

if st.button("Predict"):
    result = predict_score(transactions, savings)
    st.write(result)