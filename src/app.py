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
classifier = pickle.load(gbdt_classifier_pickle)

@app.route("/predict", methods = ["POST"])
def predict():
    predict_request = request.get_json()

    # unpacking the json object
    duration = predict_request["duration"]
    srcbytes = predict_request["srcbytes"]
    dstbytes = predict_request["dstbytes"]
    land = predict_request["land"]
    wrongfragment = predict_request["wrongfragment"]
    urgent = predict_request["urgent"]
    hot = predict_request["urgent"]
    numfailedlogins = predict_request["numfailedlogins"]
    loggedin = predict_request["loggedin"]
    numcompromised = predict_request["numcompromised"]
    rootshell = predict_request["rootshell"]
    suattempted = predict_request["suattempted"]
    numfilecreations = predict_request["numfilecreations"]
    numshells = predict_request["numshells"]
    numaccessfiles = predict_request["numaccessfiles"]
    ishostlogin = predict_request["ishostlogin"]
    count = predict_request["count"]
    srvcount = predict_request["srvcount"]
    serrorrate = predict_request["serrorrate"]
    rerrorrate = predict_request["rerrorrate"]
    samesrvrate = predict_request["samesrvrate"]
    diffsrvrate = predict_request["diffsrvrate"]
    srvdiffhostrate = predict_request["srvdiffhostrate"]
    dsthostcount = predict_request["dsthostcount"]
    dsthostsrvcount = predict_request["dsthostsrvcount"]
    dsthostdiffsrvrate = predict_request["dsthostdiffsrvrate"]
    dsthostsamesrcportrate = predict_request["dsthostsamesrcportrate"]
    dsthodtsrvdiffhostrate = predict_request["dsthodtsrvdiffhostrate"]
    protocol = predict_request["protocol"]
    service = predict_request["service"]
    flag = predict_request["flag"]
    protocol_encoded = None
    service_encoded = None
    flag_encoded = None

    # encoding protocol
    if protocol == "tcp":
        protocol_encoded = None
    elif protocol == "udp":
        protocol_encoded = None
    elif protocol == "icmp":
        protocol_encoded = None
    
    # encoding service
    if service == "ftp_data":
        service_encoded = None
    elif service == "other":
        service_encoded = None
    elif service == "private":
        service_encoded = None
    elif service == "http":
        service_encoded = None
    elif service == "remote_job":
        service_encoded = None
    elif service == "name":
        service_encoded = None
    elif service == "netbios_ns":
        service_encoded = None
    elif service == "eco_i":
        service_encoded = None
    elif service == "mtp":
        service_encoded = None
    elif service == "telnet":
        service_encoded = None
    elif service == "finger":
        service_encoded = None
    elif service == "domain_u":
        service_encoded = None
    elif service == "supdup":
        service_encoded = None
    elif service == "uucp_path":
        service_encoded = None
    elif service == "Z39_50":
        service_encoded = None
    elif service == "smtp":
        service_encoded = None
    elif service == "csnet_ns":
        service_encoded = None
    elif service == "uucp":
        service_encoded = None
    elif service == "netbios_dgm":
        service_encoded = None
    elif service == "urp_i":
        service_encoded = None
    elif service == "auth":
        service_encoded = None
    elif service == "domain":
        service_encoded = None
    elif service == "ftp":
        service_encoded = None
    elif service == "bgp":
        service_encoded = None
    elif service == "ldap":
        service_encoded = None
    elif service == "ecr_i":
        service_encoded = None
    elif service == "gopher":
        service_encoded = None
    elif service == "vmnet":
        service_encoded = None
    elif service == "systat":
        service_encoded = None
    elif service == "http_443":
        service_encoded = None
    elif service == "efs":
        service_encoded = None
    elif service == "whois":
        service_encoded = None
    elif service == "imap4":
        service_encoded = None
    elif service == "iso_tsap":
        service_encoded = None
    elif service == "echo":
        service_encoded = None
    elif service == "klogin":
        service_encoded = None
    elif service == "link":
        service_encoded = None
    elif service == "sunrpc":
        service_encoded = None
    elif service == "login":
        service_encoded = None
    elif service == "kshell":
        service_encoded = None
    elif service == "sql_net":
        service_encoded = None
    elif service == "time":
        service_encoded = None
    elif service == "hostnames":
        service_encoded = None
    elif service == "exec":
        service_encoded = None
    elif service == "ntp_u":
        service_encoded = None
    elif service == "discard":
        service_encoded = None
    elif service == "nntp":
        service_encoded = None
    elif service == "courier":
        service_encoded = None
    elif service == "ctf":
        service_encoded = None
    elif service == "ssh":
        service_encoded = None
    elif service == "daytime":
        service_encoded = None
    elif service == "shell":
        service_encoded = None
    elif service == "netstat":
        service_encoded = None
    elif service == "pop_3":
        service_encoded = None
    elif service == "nnsp":
        service_encoded = None
    elif service == "IRC":
        service_encoded = None
    elif service == "pop_2":
        service_encoded = None
    elif service == "printer":
        service_encoded = None
    elif service == "tim_i":
        service_encoded = None
    elif service == "pm_dump":
        service_encoded = None
    elif service == "red_i":
        service_encoded = None
    elif service == "netbios_ssn":
        service_encoded = None
    elif service == "rje":
        service_encoded = None
    elif service == "X11":
        service_encoded = None
    elif service == "urh_i":
        service_encoded = None
    elif service == "http_8001":
        service_encoded = None
    elif service == "aol":
        service_encoded = None
    elif service == "http_2784":
        service_encoded = None
    elif service == "tftp_u":
        service_encoded = None
    elif service == "harvest":
        service_encoded = None

    # encoding flag
    if flag == "SF":
        flag_encoded = None
    elif flag == "S0":
        flag_encoded = None
    elif flag == "REF":
        flag_encoded = None
    elif flag == "RSTR":
        flag_encoded = None
    elif flag == "SH":
        flag_encoded = None
    elif flag == "RSTO":
        flag_encoded = None
    elif flag == "S1":
        flag_encoded = None
    elif flag == "RSTOS0":
        flag_encoded = None
    elif flag == "S3":
        flag_encoded = None
    elif flag == "S2":
        flag_encoded = None
    elif flag == "OTH":
        flag_encoded = None

    # scaling the training data
    scaler = StandardScaler()
    training_data = pd.read_csv("../datasets/x_train.csv")
    training_data_scaled = scaler.fit_transform(training_data)

    model_inputs = [[duration, srcbytes, dstbytes, land, wrongfragment, urgent, hot, numfailedlogins, loggedin, numcompromised, rootshell, suattempted, numfilecreations, numshells, numaccessfiles, ishostlogin, count, srvcount, serrorrate, rerrorrate, samesrvrate, diffsrvrate, srvdiffhostrate, dsthostcount, dsthostsrvcount, dsthostdiffsrvrate, dsthostsamesrcportrate, dsthodtsrvdiffhostrate, protocol_encoded, service_encoded, flag_encoded]]

    # transforming the input data
    model_inputs = scaler.transform(model_inputs)

    result = classifier.predict(model_inputs)

    return None
