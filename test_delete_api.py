import pytest
import json
import requests

endpoint = "https://reqres.in/api/users/2"

def test_delete_request():
    response = requests.delete(endpoint)
    assert response.status_code == 204
    json_reponse = json.loads(response.text)

    print(json_reponse)

# fail due to delete request