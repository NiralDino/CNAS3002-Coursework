#This will add the root of the repository to the Python path
import sys
import os
sys.path.insert(0, os.path.abspath("."))

#This is just a test program for Jenkins
from flaskcoursework_app import app

def test_calculation_success():
    client = app.test_client()

    response = client.post(
        "/calculation",
        json={"numbers": [1, 2, 3, 4, 5]}
    )

    assert response.status_code == 200

    #If the results for the list of numbers isn't shown as below, the test would fail
    data = response.get_json()
    assert data["Mean"] == 3
    assert data["Median"] == 3
    assert data["Minimum"] == 1
    assert data["Maximum"] == 5
