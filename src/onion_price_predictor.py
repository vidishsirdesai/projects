from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def welcome_note():
    return "<h1>Onion Price Predictor App</h1>"

# @app.route("/future_forecast", methods = ["GET"])


if __name__ == "__main__":
    app.run(debug = True)