import pandas as pd
import streamlit as st
import datetime
import pickle

# reading the dataset
cars_df = pd.read_csv("./cars24.csv")

# adding a title
# st.write("# Cars24 Used Car Price Prediction")
# or can also be done in the following fashion
st.title("Cars24 Used Car Price Prediction")

# display the dataset in the application
st.header("Dataset", divider = "orange")
st.dataframe(cars_df.head())

col1, col2 = st.columns(2)

# adding a dropdown menu to select the fuel type of the car
fuel_type = col1.selectbox("Fuel Type", ["Diesel", "Petrol", "LPG", "Electric"])

# adding a slider to select the engine power
engine_power = col1.slider("Engine Power", 100, 5000, steps = 100)

# adding a dropdown menu to select the transmission type of the car
transmission_type = col2.selectbox("Transmission Type", ["Manual", "Automatic"])

# adding a dropdown menu to select the seating capacity
seating_capacity = col2.selectbox("Seating Capacity", [2, 5, 7, 9, 11])

# model inputs = year, km_driven, mileage, engine, max_power, age, make, model, Individual, Trustmark Dealer, Diesel, Electric, LPG, Petrol, Manual, 5, >5

# 
def model_pred(fuel_type, engine_power, transmission_type, seating_capacity):

    # loading the model
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
        input_features = [[]]
    return model.predict(input_features)

# the code in this block is only run if the user clicks the Predict button
if (st.button("Predict")):
    # encoding the categorical inputs into numerical

    price = model_pred()
    st.text(f"Estimated Price = {price[0].round(2)} lakh Rupees")