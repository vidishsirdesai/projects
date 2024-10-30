from flask import Flask, request

import pickle

import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route("/")
def welcome_note():
    return "<p>Hello!</p>"

# reading the trained model's pickle file
gbdt_classifier_pickle = open("../artifacts/gbdt_classifier.pkl", "rb")

# loading the classifier model
anomaly_classifier = pickle.load(gbdt_classifier_pickle)

