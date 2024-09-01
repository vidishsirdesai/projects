import streamlit as st
import yfinance as yf
import datetime as dt

# download the data using the following syntax
# data = yf.download(ticker_symbol, start = start_date, end = end_date)
# let the user define the stock name and the date range for which they want analyze the stock for

ticker_symbol = st.text_input("Enter the Stock Name", "AAPL")

# use either the following lines
# start_date = st.date_input("Start Date", value = dt.date(2019, 1, 7))
# end_date = st.date_input("End Date", value = dt.date(2023, 1, 7))

# or use the following beautified version
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start Date", value = dt.date(2019, 1, 7))

with col2:
    end_date = st.date_input("End Date", value = dt.date(2023, 1, 7))

data = yf.download(ticker_symbol, start = start_date, end = end_date)

# to show the data in the web app
st.write(data)

# visualizing
st.line_chart(data["Close"])

st.bar_chart(data["Volume"])