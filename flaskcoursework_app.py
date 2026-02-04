#This module is essential as it allows us to carry out the calculations required for the application like the mean, medium, lowest and highest numbers and standard deviation
import statistics
#Flask will be used for the web application to show the output results in JSON format, with help from the jsonify and request components
from flask import Flask, jsonify, request

#This creates the instance for Flask
app = Flask(__name__)

#This will be the URL path, where it will listen for POST requests in the API
@app.route("/calculation", methods=["POST"])

#Here is where the JSON payloads will be carried out
def calculation():
    try:
        #This will retrieve the JSON data sent by the user
        data = request.get_json()

        #The list of numbers are stored for the JSON payload
        numbers = data["numbers"]

        #This will check if the list of numbers isn't empty for JSON, if it is then the application will send an error message
        if not data or "numbers" not in data:
            return jsonify({
                "Error": "JSON requires a list of 'numbers'!"
            }), 400

        #This will check if the list of numbers is a non empty list
        if not isinstance(numbers, list) or len(numbers) == 0:
            return jsonify({
                "Error": "The list of numbers should be non empty!"
            }), 400

        #This is the same numbers only restriction from the ValueError try except block from earlier but this is applied for JSON as well
        for n in numbers:
            if not isinstance(n, (int, float)):
                return jsonify({
                    "Error": "Only numbers are allowed"
                }), 400
        
        #This will show the inputted numbers and all the calculations in JSON format
        result = {
            "Numbers": numbers,
            "Mean": statistics.mean(numbers),
            "Median": statistics.median(numbers),
            "Minimum": min(numbers),
            "Maximum": max(numbers)
        }

        #This will show the standard deviation calculation with the input validation that requires 2 numbers
        if len(numbers) >= 2:
            result["Standard Deviation"] = statistics.stdev(numbers)
        else:
            result["Standard Deviation"] = "This requires at least 2 numbers"

        return jsonify(result), 200

    #If there are any unexpected errors then it will show a message instead of crashing
    except Exception as e:
        return jsonify({
            "Error": str(e)
        }), 400

#This makes sure that Flask works when this file is compiled, the host and port will allow external access and prevents the server from starting during the tests
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port, debug=True)
