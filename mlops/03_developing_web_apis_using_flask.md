# Why Is Knowing Web Development Important For A Data Scientist?
The simple reason is that the role of a Data Scientist requires them to develop a software that makes use of AI in the background. There is no use of developing an AI model if it is not usable by the stake-holders through a web app or an interface.


# How Does An ML Idea See The Light Of The Day? The End-To-End Process Of Developing And Deploying An ML Solution
### Phase 1: Planning
1. The first thing needed to develop an ML model is data. Data can be in different formats (e.g., `.csv`, `.txt`, `.json`, etc).
2. Data cleaning, preprocessing, and EDA is performed once the relevant data that is needed is in place.
3. Requirements on what is to be done with the data are gathered.
4. A map of what is to be done, how is it to be done, and when is it to be done is drawn.
5. The output of this step is the clean data using which the model is built.

### Phase 2: Model building
1. Based on the requirements, a decision is made on what type of model is to be built to serve the requirement.
2. The model is then built, and the performance of the model is computed.
3. The areas that need improvement are researched upon, and the necessary actions are taken to improve the model's performance on the unseen data.
4. The output of this step is an ML model.

### Phase 3: Backend development
1. A backend software that includes the logic that will be served to the customer(s) is developed. Logic can be, authentication, user information filtering, basically the stuff that happens in the product owner's servers.
2. From this backend logic, APIs are built. These APIs can be accessed by the users, to ask the backend logic for whatever details it is they are looking for in the application.
3. Once the server has a response for the API endpoint, the response is returned back to the user.
4. Java, Python, NodeJS, AngularJS etc, are popularly used for building backend code.

### Phase 4: Frontend development
1. The interface with which the user is giong to interact with is built here.
2. Popularly, HTML, CSS, JavaScript, ReactJS are used in building such web interfaces.

The job of a Data Scientist ends after Phase 3, i.e., building the API.

### Note
- Whatever code that is running on the client's machine is the frontend code.
- Whatever code that is running on the server's machine is the backend code.
- Frontend code calls the API's of the backend code, then the backend code generates a response to the API that made the call. The result is then displayed to the client.


# What Are APIs?
Web APIs are are tools for making information and application functionality accessible over the internet.

In programming more generally, the term API, short for Application Programming Interface, refers to a part of a computer program designed to be used or manipulated by another program, as opposed to an interface designed to be used or manipulated by a human. Computer programs frequently need to communicate amongst themselves or with the underlying operating system, and APIs are one way they do it.

### API terminology
While building APIs, the following terms are frequently encountered,
- HTTP (Hyper Text Transfer Protocol): This the primary means of communicating data on the web. HTTP implements a number of *methods*, which tell the direction in which the data is moving in and what should happen to it. The 2 most common *methods* are, 
    - `GET`: This pulls the data from the server.
    - `POST`: This pushes new data to a server.
- URL (Uniform Resource Locator): A URL is an address for a resource on the web, such as `https://programminghistorian.org/about`. A URL consists of a protocol (`https://`), domain name (`programminghistorian.org`), and an optional path (`/about`). A URL describes the location of a specific resource, such as a web page. When reading about APIs, the terms, URL, requests, URI, or endpoint are encountered frequently, the meaning of each one is as follows,
    - URL (Uniform Resource Locator): This is the complete address of a resource on the internet, including the protocol (e.g., HTTP), domain name, path and often the query parameters. For example, `https://api.example.com/users/123`.
    - URI (Uniform Resource Identifier): This is a broader term that encompasses all the types of resources on the internet, including URLs, email addresses, and file paths. However, in the context of APIs, URI is often used interchangeably with URL.
    - Endpoint: This is the specific path or resource within an API that can be accessed. In the example above, `/users/123` is the endpoint.
    - RequestL This is a message sent from a client (e.g., a web application) to a server to request a resource or perform an action. It includes the HTTP methos (e.g., `GET`, `POST`, `PUT`, `DELETE`), headers, and sometimes a request body.
    - To summarize:
        - A URL is a specific type of URI that points to a web resource.
        - An endpoint is a part of a URL that identifies a specific resource or action within an API.
        - A request is a message sent to an API endpoint to retrieve or modify data.
- JSON (JavaScript Object Notation): JSON is a text based storage format that is designed to be easy to read for both humans and machines. JSON is generally the most common format for returning data through an API, XML being the second most common.
- REST (REpresentational State Transfer): REST is a philosophy that describes some best practices for implementing APIs. APIs designed with some or all of these principles in mind are called REST APIs.

### Client server communications
Client server communication is a fundamental model in computer networks where a client (e.g., a web browser, mobile app, or a desktop application) interacts with a server (a powerful machine) to request and receive data or services. This model forms the basis of many modern applications and services, from websites and online games to cloud computing and IoT devices.

It works in the following way,
1. Client initiates a request: The client sends a request to the server, typically using a network protocol like HTTP or TCP/IP. The request specifies the desired action or data.
2. Server processes request: The server receives the request, processes it, and prepares a response. This might involve fetching data from a database, executing a program, or performing other tasks.
3. Server sends response: The server sends a response back to the client, containing the requested data or a status indicating the success or failure of the request.
4. Client processes response: The client receives the response and interprets it. It might display the data to the user, update its state, or send another request to the server.

Common use cases are,
- Web applications: A web browser (client) sends a request to a web server, which retrives the HTML, CSS, and JavaScript files needed to render the webpage.
- Database systems: A client application (e.g., a database management tool) sends queries to a database server, which processes the queries and returns the results.
- Cloud computing: Clients can access cloud-based services (e.g., storage, computing power) by sending requests to cloud servers.
- IoT Devices: IoT devices (clients) can send data to a server for analysis or control, and the server can send commands back to the devices.

Key protocols,
- HTTP (Hypertext Transfer Protocol): The most common protocol for web-based communication.
- TCP/IP (Transmission Control Protocol/Internet Protocol): A suite of protocols that provides reliable communication over the internet.
- UDP (User Datagram Protocol): A simpler protocol that is less reliable but faster than TCP/IP.

### Popular HTTP status codes
1. 404: This code indicates "Not Found" in client-server communications. It means that the requested resource (e.g., a webpage, image, or API endpoint) could not be found on the server.
2. 200 Series: These codes indicate success. The popular ones are,
    - 200 OK: The request was successful, and the server sent the requested data.
    - 201 Created: The request was successful, and a new resource was created.
    - 202 Accepted: The request has been accepted for processing, but the processing has not been completed yet.  
    - 204 No Content: The request was successful, but there is no content to return.
3. 500 Series: These codes indicate internal server errors.
    - 500 Internal Server Error: There was an unexpected error on the server that prevented the request from being fulfilled.
    - 501 Not Implemented: The server does not support the requested method.
    - 502 Bad Gateway: The server received an invalid response from an upstream server.
    - 503 Service Unavailable: The server is temporarily unavailable due to maintenance or overload.  
    - 504 Gateway Timeout: The server did not receive a timely response from an upstream server.


# Flask
Flask is a lightweight framework that helps in developing APIs in Python.

Flask is a lightweight Python web framework. It provides a simple and flexible way to build web applications using Python. Flask is known for its minimalist approach, allowing developers to focus on the core functionality of their application without being overwhelmed by complex boilerplate code.

### Setup
1. Create a virtual environment. Refer this: https://github.com/vidishsirdesai/dsml_end_to_end_reference/blob/main/mlops/deploying_a_model_using_streamlit.ipynb.
2. Install Flask using the command, `pip install flask`.
3. Create a new file, `hello.py`.
4. Goto, https://flask.palletsprojects.com/en/3.0.x/, and open Quickstart > A Minimal Application.
5. Copy the example code into `hello.py`.
6. Once the code is copied, save the file.
7. Goto the terminal and run `FLASK_APP=hello.py flask run`.
8. Open http://127.0.0.1:5000 in the browser to view the app.

### Contents of `hello.py`
```Python
from flask import Flask

app = Flask(__name__) # a flask app is created using this syntax
# a flask app has to be created everytime a flask is being used to create API endpoints

@app.route("/") # this indicates the endpoint about where the endpoint can be found
# meaning if it were @app.route("/hello"), this indicates that the endpoint can be found at "/hello"
# this is a decorator which tells to execute a function whenever a specified endpoint is encountered
def hello_world():
    return "<p>Hello, World!</p>"
```

### What's happening in the background?
There are 4 types of requests in the REST APIs.
- `GET`: The `GET` request or method is executed whenever a URL is entered, and no other information is passed. For example, when http://www.google.com/ is entered, a `GET` request is executed. In simple words, `GET` is used to access some resource from a server.
- `POST`: `POST` request or method is executed whenever some resource is being sent to a server. For example, while logging in, username and password has to be entered. This is when a `POST` request is executed. In simple words, `POST` is used to send some information to a server.
- `PUT`: `PUT` is used to update an existing information in a server.
- `DELETE`: `DELETE` is used to delete an existing information in a server.

The difference between `GET` and `POST` is that, in the `POST` request as there is a need to upload some information to a server, a body with the URL is needed. `GET` on the other hand has only the URL.

Download and install Postman: https://www.postman.com/downloads/

Inside Postman,
1. Create an account/ Login to an account.
2. Click on Send an API request (or) `command + T` on Mac.
3. Set the request method to `GET`.
4. Enter the URL, i.e., http://127.0.0.1:5000, and observe the output.


# University Admissing Predictor App
1. Use the `dataset_admission_prediction.csv` to perform EDA, feature engineering and build a model.
2. Store the model in a pickle file, `model.pkl`. The model files should always be stored inside `./artifacts` directory.
3. Create a new file with the name, `predict.py`.
4. Once everything is in place, run using the command, `FLASK_APP=predict.py flask run`.
5. Open the browser, and paste the URl, http://127.0.0.1:5000/predict. A prompt which says, "Method Not Allowed" is displayed on the browser window. This is because any URL run from the search tab of the browser runs a GET method. But the app is expecting a POST request.
6. Open Postman, change the request method to POST, and paste the same URL, i.e., http://127.0.0.1:5000/predict.
7. Click on Body, and select raw, and then select JSON. [All the network calls popularly happen in JSON format].
8. Pass the parameters in the dictionary format, `{"gre_score": 300, "toefl_score": 100, "university_rating": 4, "sop": 3, "lor": 4, "cgpa": 8.90, "research": "Yes"}`.
9. Click on send to get the response.
10. The API endpoints can now be given to a front-end developer for him to build a software on top of this.

### Contents of `predict.py`
```Python
from flask import Flask, request
import pickle
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# read the model file
model_pickle = open("./artifacts/model.pkl", "rb")

# load the model into a variable called regressor
regressor = pickle.load(model_pickle)

# define a prediction method
# define a decorator to set that the following method is related/ connected to an API endpoint
# a GET method will not work here because the model inputs have to be fetched from the client machine
@app.route("/predict", methods = ["POST"])
def prediction():
    # the body of the POST request made by the user has to be fetched and stored into some variable, because this is required to make the prediction
    # request.get_json() will have all the json information present within the body that was sent by the user
    prediction_request = request.get_json()
    # the information sent from the clients end is in JSON format

    # if the information fetched has some data that should be to encoded into the correct format then do so
    # the other information that has been sent should be unpacked and stored into different variables
    # in case of this example there is no data that should be encoded, the data sent should only be unpacked and stored into separate variables

    # unpacking
    gre_score = prediction_request["gre_score"]
    toefl_score = prediction_request["toefl_score"]
    university_rating = prediction_request["university_rating"]
    sop = prediction_request["sop"]
    lor = prediction_request["lor"]
    cgpa = prediction_request["cgpa"]
    research = prediction_request["research"]

    # encoding
    if research == "Yes":
        research = 1
    else:
        research = 0

    # scaling the train data
    scaler = StandardScaler()
    train = pd.read_csv("train.csv")
    train = scaler.fit_transform(train)

    # to get the final result, the clf method has to be called with all the variables that have been extracted
    model_inputs = [[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]]

    # scaling the model_inputs
    model_inputs = scaler.transform(model_inputs)

    result = regressor.predict(model_inputs)

    # the prediction has to be converted to JSON format in order for it to be returned back to the user
    return {"chance_of_admit": result[0]}
```