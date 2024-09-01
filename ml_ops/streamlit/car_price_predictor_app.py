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
diesel = 0
petrol = 0
lpg = 0
electric = 0
if fuel_type == "Diesel":
    diesel = 1
    petrol = 0
    lpg = 0
    electric = 0
elif fuel_type == "Petrol":
    diesel = 0
    petrol = 1
    lpg = 0
    electric = 0
elif fuel_type == "LPG":
    diesel = 0
    petrol = 0
    lpg = 1
    electric = 0
else:
    diesel = 0
    petrol = 0
    lpg = 0
    electric = 1

# adding a slider to select the engine power
engine_power = col1.slider("Engine Power", 100, 5000, step = 100)

# adding a dropdown menu to select the seating capacity
seating_capacity = col2.selectbox("Seating Capacity", [2, 5, 7, 9, 11])
if seating_capacity > 5:
    lesser_than_5 = 0
    greater_than_5 = 1
else:
    lesser_than_5 = 1
    greater_than_5 = 0

# adding a slider to select the age
age = col2.slider("Age", 0, 40, step = 1)

# model inputs = year, km_driven, mileage, engine, max_power, age, make, model, Individual, Trustmark Dealer, Diesel, Electric, LPG, Petrol, Manual, 5, >5

# defining a function to read the stored model and make predictions
def model_pred(engine_power, age, diesel, electric, lpg, petrol, lesser_than_5, greater_than_5):
    # loading the model
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
        model_inputs = [[2012.0, 120000, 19.7, engine_power, 46.3, age, 5.458819, 3.394000, 1, 0, 0, diesel, electric, lpg, petrol, lesser_than_5, greater_than_5]]
    return model.predict(model_inputs)

# the code in this block is only run if the user clicks the Predict button
if (st.button("Predict")):
    price = model_pred(engine_power, age, diesel, electric, lpg, petrol, lesser_than_5, greater_than_5)
    st.text(f"Estimated Price = {price[0].round(2)} lakh Rupees")

    # the prediction is way off, expect an update soon. Thanks :)