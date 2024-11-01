import pytest
from predict import app

# creating a test client instance to simulate the HTTP requests
@pytest.fixture
def client():
    return app.test_client()

# 
def test_ping(client):
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json == {"MESSAGE: Ping successful."}


def test_prediction(client):
    test_data = {
        "duration": 38044,
        "srcbytes": 1,
        "dstbytes": 0,
        "land": 0,
        "wrongfragment": 0,
        "urgent": 0,
        "hot": 0,
        "numfailedlogins": 0,
        "loggedin": 0,
        "numcompromised": 0,
        "rootshell": 0,
        "suattempted": 0,
        "numfilecreations": 0,
        "numshells": 0,
        "numaccessfiles": 0,
        "ishostlogin": 0,
        "count": 2,
        "srvcount": 2,
        "serrorrate": 0.0,
        "rerrorrate": 1.0,
        "samesrvrate": 1.0,
        "diffsrvrate": 0.0,
        "srvdiffhostrate": 0.0,
        "dsthostcount": 255,
        "dsthostsrvcount": 2,
        "dsthostdiffsrvrate": 0.5,
        "dsthostsamesrcportrate": 1.0,
        "dsthostsrvdiffhostrate": 0.0,
        "protocol": "tcp",
        "service": "Z39_50",
        "flag": "RSTR"
    }
    resp = client.post("/classify_attack_type", json = test_data)
    assert resp.status_code == 200
