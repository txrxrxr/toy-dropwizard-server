import requests
import pytest # have to install via command "pip3 install -U pytest"

def test_health_check():
    r = requests.get('http://localhost:8085')
    assert(r.status_code == 404)

# 1. Add two more tests here of your choice. I will explain the API.
#    Make sure to verify the necessary info, e.g., status code, response data.
# 2. Add "pytest" as integration testing script as part of Github Actions CI workflow (you've done this before!)

def test_status_code():
    r = requests.get('http://localhost:8085/hello-world?name=txr')
    assert(r.status_code == 200)

def test_content():
    r = requests.get('http://localhost:8085/hello-world?name=txr')
    assert(r.json()['content'] == 'Hello, txr!')