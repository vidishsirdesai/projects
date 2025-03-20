# What Is Streamlit?
Streamlit is a Python tool that helps in building a website in no time. It is not a requirement for a Data Scientist to know front-end and back-end development and the connections between them, this is a job of a Software Developer. But, it is an essential requirement for a Data Scientist to show the working of a model, with visualizations included, to the stake holders. In this case, building a simple application that allows the user to interact with the various parameters and visualize the output etc, becomes essential.

Streamlit serves exactly this requirement of a Data Scientist without him/ her known the fundamentals of web development (front-end and back-end).

Streamlit is popularly by used by Data Scientists and Analysts for building a POC (proof of concept) app.


# Setup
### Prerequisites
1. Python version 3.8 to 3.12.
2. A Python environment manager: Environment managers create virtual environments to isolate Python package installations between projects. It is recommended that virtual environments be used because installing or upgrading a Python package may cause unintentional effects on another package. Here, venv is used.
3. A Python package manager, popularly pip is the go to one.
4. A code editor, like VS Code.

### Create a virtual environment `venv`
1. `cd <project_folder_path>`.
2. `pip install virtualenv`.
3. `python3 -m venv .venv`.
4. A folder named `.venv` will appear in the project directory. The project directory is where the virtual environment and its dependencies are installed.

But before an environment is created, create a "`requirements.txt`" file that contains all the dependencies that the app will need to run. Include the following lines inside `requirements.txt`,

```text
streamlit
scikit-learn
numpy
pandas
```

### Activate the virtual environment
In the terminal, activate the environment with one of the following commands depending on the operating system,
- Windows command prompt, `.venv\Scripts\activate.bat`.
- Windows PowerShell, `.venv\Scripts\Activate.ps1`.
- MacOS and Linux source `.venv/bin/activate`.

Once activated, the environment name can be seen in the parentheses before the prompt "`(.venv)`".

Once `requirements.txt` file is created and the virtual environment is activated, run the following command to install the dependencies,
- `pip install -r requirements.txt`.

### Deactivate the virtual environment
Strictly run the following 2 commands in the same order,
1. `deactivate`.
2. `rm -r .venv`.

### Install `streamlit` in the virtual environment
1. `pip install streamlit`.
2. Test if the installation has worked, `streamlit hello`. If this does not work, use the long-form command, `python -m streamlit hello`.
3. Streamlit's hello app should open in a new tab in the browser.

### Build an application
1. Goto the Streamlit's website > Docs > Develop > API reference > Text elements > st.header
2. Create a new file `app.py`.
3. Copy the contents of the examples under `st.header`.
4. To run this using the command, `streamlit run app.py`. If this does not work, try the long-form command, `python -m streamlit run app.py`.
5. To stop the Streamlit server, press `Ctrl + C` in the terminal.

### Contents Of `app.py`
```Python
import streamlit as st

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("This is a subheader with a divider", divider="gray")
st.subheader("These subheaders have rotating dividers", divider=True)
st.subheader("One", divider=True)
st.subheader("Two", divider=True)
st.subheader("Three", divider=True)
st.subheader("Four", divider=True)
```


# Stock Market Data App
1. Create a file `stock_market_app.py`.
2. Install the yfinance package, `pip install yfinance`.
3. Once the code is in place, run the app, `streamlit run stock_market_app.py`.

### Contents of `stock_market_app.py`
```Python
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
```


# University Addmission Predictor App
1. Create a file `admission_predictor_app.py`.
2. This app is being built for a student who want to find out their chance of admission to a University.
3. The target variable is "chance_of_admission".

### Approach
1. To begin with, a `.csv` file containing the features and target variable is given.
2. EDA.
3. Build a model (linear regression in this case).
4. Save this model using `pickle`.
5. Load the model using `pickle`.
6. Build the streamlit app that uses the model.
7. Deploy the model in cloud for use.
8. `streamlit run admissing_predictor_app.py`.

### Contents of `admission_predictor_app.py`
```Python
import pandas as pd
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler

# reading the dataset
df = pd.read_csv("./dataset.csv")

# adding a title
# st.write("# Predicting the Chance of Admission")
# or can also be done in the following fashion
st.title("Predicting the Chance of Admission")

# display the dataset in the application
st.header("Dataset", divider = "orange")
st.dataframe(df.head())

col1, col2, col3 = st.columns(3)

# adding a slider to set the gre_score
gre_score = col1.slider("GRE Score", 200, 400, step = 1)

# adding a slider to set the toefl_score
toefl_score = col2.slider("TOEFL Score", 0, 150, step = 1)

# adding a slider to set the university_rating
university_rating = col1.slider("University Rating", 0, 5, step = 1) 

# adding a slider to set the sop
sop = col2.slider("SOP", 0, 5, step = 1)

# adding a slider to set the lor
lor = col1.slider("LOR", 0, 5, step = 1)

# adding a slider to set the cgpa
cgpa = col2.slider("CGPA", 0.00, 10.00, step = 0.01)

# adding a dropdown menu to set the research
research = st.selectbox("Research", ["Yes", "No"])
if research == "Yes":
    research = 1
else:
    research = 0

# model inputs = [gre_score, toefl_score, university_rating, sop, lor, cgpa, research]

# defining a function to read the stored model and make predictions
def model_pred(gre_score, toefl_score, university_rating, sop, lor, cgpa, research):
    # loading the model
    with open("train.csv", "rb") as file:
        train = pd.read_csv("train.csv")
        scaler = StandardScaler()
        train = scaler.fit_transform(train)

    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
        model_inputs = [[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]]
        model_inputs = scaler.transform(model_inputs)

    return model.predict(model_inputs)

# the code in this block is only run if the user clicks the Predict button
if (st.button("Predict")):
    prediction = model_pred(gre_score, toefl_score, university_rating, sop, lor, cgpa, research)
    st.text(f"Chance of Admit = {prediction}")
```


# Deploying The App
1. To deploy, it is required that the app and its dependencies have to be pushed to GitHub.
2. Goto `share.streamlit.io` and create an account.
3. Click on "Create app" located on the top right corner of the home page.
4. A window pops up, with a the prompt, "You must be connected to GitHub to deploy an app".
5. Click on "Connect to GitHub", and complete the authorization.
6. Under "Do you already have an app?", select "Yup, I have an app".
7. Fill the following fields, Repository, Branch, Main file path, App URL (optional).
8. Click "Deploy!", and voila the app is up and running. The link can now be shared and anyone can use it.