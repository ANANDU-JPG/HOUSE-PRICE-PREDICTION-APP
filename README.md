# HOUSE-PRICE-PREDICTION-APP
A simple machine learning project that predicts house prices based on size and number of bedrooms.
It includes:

A Linear Regression model built using scikit-learn

A Streamlit web app for user-friendly predictions

A saved model file (house_price_model.pkl) that the app loads automatically
 Features

 Custom Housing Dataset
 Linear Regression Model (trained with scikit-learn)
 Pickle Model Saving
 Streamlit Web Interface
 Instant live predictions
 Clean and easy-to-understand project structure
 
 Project Structure

├── app.py                     
├── train_model.py             
├── house_price_model.pkl
├── README.md                  

Training Script — train_model.py
Builds a DataFrame
Splits data
Trains Linear Regression
Saves the model

 Web App — app.py
Loads model
Takes user input
Uses model.predict()
Displays formatted price
