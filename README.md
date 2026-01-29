For our coursework I've coded 2 Python files. These Python calculator applications will carry out calculations from a list of numbers that is provided by user input, afterwards the applications will do the calculations (mean, median, minimum, maximum and standard deviation) and print them out however the Flask application will show the results in a different way which will be discussed later. 

The normal application will run within the terminal with the python3 command, when it's running it will ask for the list of numbers with user input where you have to give a space in between, this will let the app know which numbers will be saved and the spaces are ignored. Afterwards the calculations are carried out with that list of numbers and results are shown on the terminal. 
There is a try again function as well if you want to do more calculations or if you get error messages from input validation, such as if you try to enter in any character other than numbers it will show a message saying to only enter numbers and the try again function comes where it prints a message if you want to run the calculator again and you respond with a y which will run the app again or n where it will terminate the running app. Aonther input validation policy includes requiring 2 numbers for standard deviation. 
Here's how it should run normally

devasc@labvm:~/Documents/coursework/CNAS3002-Coursework$ python3 coursework.py 
Welcome to the calculator for the mean, median, minimum, maximum and standard deviation! 

Please enter your list of numbers with a space in between: 1 2 3 4 5
From the list of numbers that you've provided, here are all of your answers below: 

The mean (average) is:  3 

The median (middle number as the list of numbers are arranged in ascending order) is:  3 

The minimum (smallest) number is:  1 

The maximum (largest) number is:  5 

The standard deviation is:  1.5811388300841898 

Would you like to try again? (y/n): y
Welcome to the calculator for the mean, median, minimum, maximum and standard deviation! 

Please enter your list of numbers with a space in between: 1 2 3 4 5
From the list of numbers that you've provided, here are all of your answers below: 

The mean (average) is:  3 

The median (middle number as the list of numbers are arranged in ascending order) is:  3 

The minimum (smallest) number is:  1 

The maximum (largest) number is:  5 

The standard deviation is:  1.5811388300841898 

Would you like to try again? (y/n): n
Goodbye, thank you and come again please!
devasc@labvm:~/Documents/coursework/CNAS3002-Coursework$ 

Here's how the input validation works

devasc@labvm:~/Documents/coursework/CNAS3002-Coursework$ python3 coursework.py 
Welcome to the calculator for the mean, median, minimum, maximum and standard deviation! 

Please enter your list of numbers with a space in between: 1
From the list of numbers that you've provided, here are all of your answers below: 

The mean (average) is:  1 

The median (middle number as the list of numbers are arranged in ascending order) is:  1 

The minimum (smallest) number is:  1 

The maximum (largest) number is:  1 

Standard Deviation requires at least 2 numbers, please add more numbers.

Would you like to try again? (y/n): y
Welcome to the calculator for the mean, median, minimum, maximum and standard deviation! 

Please enter your list of numbers with a space in between: 1 d
You have entered an letter! Only enter numbers please.

Would you like to try again? (y/n): n
Goodbye, thank you and come again please!
devasc@labvm:~/Documents/coursework/CNAS3002-Coursework$ 

With the Flask application it's essentially the same mechanics however JSON payloads are implemented here as the results are shown in JSON format within a web server on local host. How it works is you run the app on 1 terminal and then on a different terminal you use the curl command where you specify the POST method onto the given URL on Flask with a specified path as well to recieve the results, then you specify the JSON format as the content type and then input your list of numbers as JSON with seperating commas, when running that command the results will show up in JSON format and on the Flask app it says it works with a POST 200 success message log. The same input validation from the original app works here as well with the single number message for standard deviation, and there's a 400 bad request message if you try to use different characters as well.

Here's how it all works with the 2 terminals

devasc@labvm:~/Documents/coursework$ python3 flaskcoursework.py 
 * Serving Flask app "flaskcoursework" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 850-504-032
127.0.0.1 - - [29/Jan/2026 12:19:30] "POST /calculation HTTP/1.1" 200 -
   
devasc@labvm:~/Documents/coursework$ curl -X POST http://127.0.0.1:5000/calculation -H "Content-Type: application/json" -d "{\"numbers\": [1, 2, 3, 4, 5]}"
{
  "Maximum": 5, 
  "Mean": 3, 
  "Median": 3, 
  "Minimum": 1, 
  "Numbers": [
    1, 
    2, 
    3, 
    4, 
    5
  ], 
  "Standard Deviation": 1.5811388300841898
}
devasc@labvm:~/Documents/coursework$ 

Here's how the input validation works

127.0.0.1 - - [29/Jan/2026 12:26:57] "POST /calculation HTTP/1.1" 200 -

127.0.0.1 - - [29/Jan/2026 12:27:08] "POST /calculation HTTP/1.1" 400 -

devasc@labvm:~/Documents/coursework$ curl -X POST http://127.0.0.1:5000/calculation -H "Content-Type: application/json" -d "{\"numbers\": [1]}"
{
  "Maximum": 1, 
  "Mean": 1, 
  "Median": 1, 
  "Minimum": 1, 
  "Numbers": [
    1
  ], 
  "Standard Deviation": "This requires at least 2 numbers"
}

devasc@labvm:~/Documents/coursework$ curl -X POST http://127.0.0.1:5000/calculation -H "Content-Type: application/json" -d "{\"numbers\": [1, d]}"
{
  "Error": "400 Bad Request: Failed to decode JSON object: Expecting value: line 1 column 17 (char 16)"
}
devasc@labvm:~/Documents/coursework$ 
