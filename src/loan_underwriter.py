import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Loan Underwriter App</h1>"

# reading the trained model's pickle file
lgr_model = open("../artifacts/lgr_model.pkl", "rb")

# loading the classifier
classifier = pickle.load(lgr_model)

@app.route("/classify", methods = ["POST"])
def classify():
    classify_request = request.get_json()

    return None

if __name__ == "__main__":
    app.run(debug = True)