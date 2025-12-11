
import streamlit as st
import pickle
import numpy as np


model = pickle.load(open("house_price_model.pkl", "rb"))

st.title(" House Price Prediction App")
st.write("Enter house details and get a predicted price!")

size = st.number_input("House size (sq ft)", min_value=300, max_value=5000, value=1200)
bedrooms = st.number_input("Number of bedrooms", min_value=1, max_value=10, value=3)

if st.button("Predict Price"):
    input_data = np.array([[size, bedrooms]])
    prediction = model.predict(input_data)
    
    st.success(f"Estimated House Price: **${prediction[0]:,.2f}**")





