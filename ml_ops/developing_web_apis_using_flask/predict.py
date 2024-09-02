from flask import Flask, request
import pickle
import sklearn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# read the model file
model = open("./artefacts/model.pkl", "rb")

# load the model
clf = pickle.load(model)

# define a prediction method
@app.route("/predict", methods = ["POST"])
def prediction():
    # the request made by the user has to be fetched, because this is required to make the prediction
    loan_req = request.get_json() # request.get_json() will have all the json information present within the body that was sent by the user
    # the information sent from the clients end is in JSON format

    # this information fetched has to encoded into the correct format
    


    # the other information that has been sent should also be saved into variables

    # to get the final result, the clf method has to be called with all the variables that have been extracted
    result = clf.predict()

    # the result has to be converted from 0 or 1 to "Rejected" or "Approved" respectively
    pred = None

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    # the prediction has to be converted to JSON format in order for it to be returned back to the user
    return {"loan_approval_status": pred}