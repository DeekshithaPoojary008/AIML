import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("house_model.pkl")

st.set_page_config(
    page_title="California House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 California House Price Prediction")
st.write("Enter the house details below to predict the median house value.")

# Input fields
median_income = st.number_input(
    "Median Income",
    min_value=0.0,
    value=3.5,
    step=0.1
)

housing_median_age = st.number_input(
    "Housing Median Age",
    min_value=1,
    value=25
)

total_rooms = st.number_input(
    "Total Rooms",
    min_value=1,
    value=2000
)

latitude = st.number_input(
    "Latitude",
    value=34.0,
    step=0.01,
    format="%.2f"
)

longitude = st.number_input(
    "Longitude",
    value=-118.0,
    step=0.01,
    format="%.2f"
)

# Prediction
if st.button("Predict House Price"):

    features = np.array([[
        median_income,
        housing_median_age,
        total_rooms,
        latitude,
        longitude
    ]])

    prediction = model.predict(features)

    st.success(
        f"Predicted Median House Value: ${prediction[0]:,.2f}"
    )