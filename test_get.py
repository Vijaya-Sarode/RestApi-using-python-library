import requests
import json
import pytest

endpoint = "https://reqres.in/api/users?page=2"

def test_get_APIenpoint():
    reponse = requests.get(endpoint)
    assert reponse.status_code == 200
    print(reponse)