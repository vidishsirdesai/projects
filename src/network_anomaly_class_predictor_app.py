from flask import Flask, request

import pickle

import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route("/")
def welcome_note():
    return "<p>Network anomaly class predictor</p>"

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
    dsthostsrvdiffhostrate = predict_request["dsthostsrvdiffhostrate"]
    protocol_encoded = predict_request["protocol_encoded"]
    service_encoded = predict_request["service_encoded"]
    flag_encoded = predict_request["flag_encoded"]

    # encoding protocol_encoded
    if protocol_encoded == "tcp":
        protocol_encoded = 80114.28824898
    elif protocol_encoded == "udp":
        protocol_encoded = 141.21503368
    elif protocol_encoded == "icmp":
        protocol_encoded = 342.94156001
    
    # encoding service_encoded
    if service_encoded == "ftp_data":
        service_encoded = 143597.02653061223
    elif service_encoded == "other":
        service_encoded = 312548.73411332874
    elif service_encoded == "private":
        service_encoded = 90075.67057154624
    elif service_encoded == "http":
        service_encoded = 6006.81136893252
    elif service_encoded == "remote_job":
        service_encoded = 0.01282051282051282
    elif service_encoded == "name":
        service_encoded = 0.0022172949002217295
    elif service_encoded == "netbios_ns":
        service_encoded = 0.002881844380403458
    elif service_encoded == "eco_i":
        service_encoded = 11.793976429506765
    elif service_encoded == "mtp":
        service_encoded = 0.002277904328018223
    elif service_encoded == "telnet":
        service_encoded = 190410.34806629835
    elif service_encoded == "finger":
        service_encoded = 392462.37577815505
    elif service_encoded == "domain_u":
        service_encoded = 130.25666261196506
    elif service_encoded == "supdup":
        service_encoded = 0.001838235294117647
    elif service_encoded == "uucp_path":
        service_encoded = 0.001451378809869376
    elif service_encoded == "Z39_50":
        service_encoded = 0.001160092807424594
    elif service_encoded == "smtp":
        service_encoded = 32667.764255435526
    elif service_encoded == "csnet_ns":
        service_encoded = 0.001834862385321101
    elif service_encoded == "uucp":
        service_encoded = 0.05384615384615385
    elif service_encoded == "netbios_dgm":
        service_encoded = 0.0024691358024691358
    elif service_encoded == "urp_i":
        service_encoded = 134.14285714285714
    elif service_encoded == "auth":
        service_encoded = 11.256544502617801
    elif service_encoded == "domain":
        service_encoded = 55.479789103690685
    elif service_encoded == "ftp":
        service_encoded = 789039.1043329532
    elif service_encoded == "bgp":
        service_encoded = 0.0014084507042253522
    elif service_encoded == "ldap":
        service_encoded = 0.0
    elif service_encoded == "ecr_i":
        service_encoded = 878.9954427083334
    elif service_encoded == "gopher":
        service_encoded = 0.7915057915057915
    elif service_encoded == "vmnet":
        service_encoded = 0.0016207455429497568
    elif service_encoded == "systat":
        service_encoded = 0.0020964360587002098
    elif service_encoded == "http_443":
        service_encoded = 0.0
    elif service_encoded == "efs":
        service_encoded = 0.002061855670103093
    elif service_encoded == "whois":
        service_encoded = 0.001443001443001443
    elif service_encoded == "imap4":
        service_encoded = 1045.9876352395672
    elif service_encoded == "iso_tsap":
        service_encoded = 0.001455604075691412
    elif service_encoded == "echo":
        service_encoded = 0.029953917050691243
    elif service_encoded == "klogin":
        service_encoded = 0.0023094688221709007
    elif service_encoded == "link":
        service_encoded = 0.002105263157894737
    elif service_encoded == "sunrpc":
        service_encoded = 0.049868766404199474
    elif service_encoded == "login":
        service_encoded = 98.89044289044288
    elif service_encoded == "kshell":
        service_encoded = 0.0033444816053511705
    elif service_encoded == "sql_net":
        service_encoded = 0.004081632653061225
    elif service_encoded == "time":
        service_encoded = 0.5030581039755352
    elif service_encoded == "hostnames":
        service_encoded = 0.002173913043478261
    elif service_encoded == "exec":
        service_encoded = 0.014767932489451477
    elif service_encoded == "ntp_u":
        service_encoded = 96.0
    elif service_encoded == "discard":
        service_encoded = 1155332.1003717473
    elif service_encoded == "nntp":
        service_encoded = 0.10472972972972973
    elif service_encoded == "courier":
        service_encoded = 0.0013623978201634877
    elif service_encoded == "ctf":
        service_encoded = 0.0017761989342806395
    elif service_encoded == "ssh":
        service_encoded = 165.6816720257235
    elif service_encoded == "daytime":
        service_encoded = 0.06333973128598848
    elif service_encoded == "shell":
        service_encoded = 5525.307692307692
    elif service_encoded == "netstat":
        service_encoded = 0.002777777777777778
    elif service_encoded == "pop_3":
        service_encoded = 2761.4583333333335
    elif service_encoded == "nnsp":
        service_encoded = 0.0
    elif service_encoded == "IRC":
        service_encoded = 13334.684491978609
    elif service_encoded == "pop_2":
        service_encoded = 3.9358974358974357
    elif service_encoded == "printer":
        service_encoded = 2.0579710144927534
    elif service_encoded == "tim_i":
        service_encoded = 504.875
    elif service_encoded == "pm_dump":
        service_encoded = 473.6
    elif service_encoded == "red_i":
        service_encoded = 91.0
    elif service_encoded == "netbios_ssn":
        service_encoded = 0.052486187845303865
    elif service_encoded == "rje":
        service_encoded = 0.011627906976744186
    elif service_encoded == "X11":
        service_encoded = 3824927.5616438356
    elif service_encoded == "urh_i":
        service_encoded = 40.7
    elif service_encoded == "http_8001":
        service_encoded = 0.0
    elif service_encoded == "aol":
        service_encoded = 0.0
    elif service_encoded == "http_2784":
        service_encoded = 0.0
    elif service_encoded == "tftp_u":
        service_encoded = 1.0
    elif service_encoded == "harvest":
        service_encoded = 0.0

    # encoding flag_encoded
    if flag_encoded == "SF":
        flag_encoded = 20938.455295185224
    elif flag_encoded == "S0":
        flag_encoded = 0.02536512582135376
    elif flag_encoded == "REJ":
        flag_encoded = 0.0
    elif flag_encoded == "RSTR":
        flag_encoded = 889347.3907476249
    elif flag_encoded == "SH":
        flag_encoded = 0.0
    elif flag_encoded == "RSTO":
        flag_encoded = 444704.5544174136
    elif flag_encoded == "S1":
        flag_encoded = 77117.35342465753
    elif flag_encoded == "RSTOS0":
        flag_encoded = 36582897.84466019
    elif flag_encoded == "S3":
        flag_encoded = 252670.02040816325
    elif flag_encoded == "S2":
        flag_encoded = 50189.88976377953
    elif flag_encoded == "OTH":
        flag_encoded = 1931.5

    # scaling the training data
    scaler = StandardScaler()
    training_data = pd.read_csv("../datasets/x_train.csv", header = 0)
    training_data.drop(columns = ["Unnamed: 0"], inplace = True)
    training_data_scaled = scaler.fit_transform(training_data)

    model_inputs = pd.DataFrame([[duration, srcbytes, dstbytes, land, wrongfragment, urgent, hot, numfailedlogins, loggedin, numcompromised, rootshell, suattempted, numfilecreations, numshells, numaccessfiles, ishostlogin, count, srvcount, serrorrate, rerrorrate, samesrvrate, diffsrvrate, srvdiffhostrate, dsthostcount, dsthostsrvcount, dsthostdiffsrvrate, dsthostsamesrcportrate, dsthostsrvdiffhostrate, protocol_encoded, service_encoded, flag_encoded]], columns = training_data.columns)

    # transforming the input data
    model_inputs = scaler.transform(model_inputs)
    
    # predict the class of attack
    result = str(classifier.predict(model_inputs)[0])

    if result == "0":
        return {"Attack Type": "Normal"}
    elif result == "1":
        return {"Attack Type": "DoS"}
    elif result == "2":
        return {"Attack Type": "R2L"}
    elif result == "3":
        return {"Attack Type": "Probe"}
    elif result == "4":
        return {"Attack Type": "U2R"}
    else:
        return {"Attack Type": "Not recognized"}

if __name__ == "__main__":
    app.run(debug = True)
