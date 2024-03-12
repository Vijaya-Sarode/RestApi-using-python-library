import requests
import pytest
import json
endpoint = "https://reqres.in/api/users"

payload ={
    "name": "morpheus",
    "job": "zion resident"
}

def test_put_request():
    reponse = requests.put(endpoint+"/api/users/2",json=payload)
    assert reponse.status_code == 200
    json_reponse = json.loads(reponse.text)
    