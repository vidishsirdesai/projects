from flask import Flask

app = Flask(__name__) # a flask app is created using this syntax
# a flask app has to be created everytime a flask is being used to create API endpoints

@app.route("/") # this indicates the endpoint about where the endpoint can be found
# meaning if it were @app.route("/hello"), this indicates that the endpoint can be found at "/hello"
# this is a decorator which tells to execute a function whenever a specified endpoint is encountered
def hello_world():
    return "<p>Hello, World!</p>"