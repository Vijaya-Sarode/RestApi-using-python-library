import requests
import json
import pytest

payload ={
    "name": "morpheus",
    "job": "leader"
}
endpoint = "https://reqres.in/api/users"
def test_post_request():
    response = requests.post(endpoint,json=payload)
    assert response.status_code ==201
    json_response = json.loads(response.text)
    print(json_response)
    