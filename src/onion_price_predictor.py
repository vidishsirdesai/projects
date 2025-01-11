from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("templates/index.html")

# @app.route("/future_forecast", methods = ["GET"])
# def future_forecast():
#     pass


if __name__ == "__main__":
    app.run(debug = True)