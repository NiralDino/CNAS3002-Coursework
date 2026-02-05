#This will add the root of the repository to the Python path
import sys
import os
sys.path.insert(0, os.path.abspath("."))

#This is just a test program for Jenkins
from flaskcoursework_app import app

#Unit test is implemented to test the Flask app
import unittest

class TestCalculationEndpoint(unittest.TestCase):
    def setUp(self):
        """
        This method will run before each test.
        It creates a FLask test client that sends HTTP requests to the application without starting a server.
        """
        self.client = app.test_client()
        self.client.testing = True

    def test_calculation_success(self):
        """
        This test checks that the /calculation endpoint compiles valid numeric input and returns the expected results
        """
        response = self.client.post(
            "/calculation",
            json={"numbers": [1, 2, 3, 4, 5]}
        )
        
        self.assertEqual(response.status_code, 200)

        #If the results for the list of numbers isn't shown as below, the test would fail
        data = response.get_json()
        self.assertEqual(data["Mean"], 3)
        self.assertEqual(data["Median"], 3)
        self.assertEqual(data["Minimum"], 1)
        self.assertEqual(data["Maximum"], 5)
        self.assertAlmostEqual(data["Standard Deviation"], 1.5811, places=4)
        
    def test_calculation_invalid_input(self):
        """
        This will check for invalid input
        """
        response = self.client.post(
            "/calculation",
            json={"numbers": [1, "a", 3]}
        )

        self.assertEqual(response.status_code, 400)
        
#This allows the test file to be run from Jenkins
if __name__ == "__main__":
    unittest.main()
