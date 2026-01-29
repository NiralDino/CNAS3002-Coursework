#This module is essential as it allows us to carry out the calculations required for the application like the mean, medium, lowest and highest numbers and standard deviation
import statistics

#The while loop is there so that if the user wants to use the calculator again, the loop repeats itself, if not then the application will stop
while True:
    #I've implemented a try/except block for the application, this is so that if the user enters a letter by any chance a ValueError shows up and a message is shown for that instead of the appliction usually crashing
    try:
        print("Welcome to the calculator for the mean, median, minimum, maximum and standard deviation! \n")
        
        #Here is where the user will input their list of numbers with a space in between, with map and split the application will know which are the numbers to be saved from the spaces that are split in between, then those numbers are on a list, after that it's saved for the calculations
        user_input = input("Please enter your list of numbers with a space in between: ")
        numbers = list(map(int, user_input.split()))

        print("From the list of numbers that you've provided, here are all of your answers below: \n" )

        #Here's all the print statements with each calculation
        print("The mean (average) is: " , statistics.mean(numbers) , "\n")
        print("The median (middle number as the list of numbers are arranged in ascending order) is: ", statistics.median(numbers) , "\n")
        print("The minimum (smallest) number is: " , min(numbers) , "\n")
        print("The maximum (largest) number is: " , max(numbers) , "\n")

        #This if statement is for when the user only entered 1 number for the list, it won't work as standard deviations needs more than 1 number
        if len(numbers) >= 2:
            print("The standard deviation is: " , statistics.stdev(numbers) , "\n")
        else:
            print("Standard Deviation requires at least 2 numbers, please add more numbers.\n")

    #When the user enters a letter in the list, instead of crashing there will be a message and the application will start again
    except ValueError:
        print("You have entered an letter! Only enter numbers please.\n")

    #This loop is a try again functionality where the user can choose if they want to use the calculator again (the while loop repeats itself), if not then the application stops running
    again = input("Would you like to try again? (y/n): ").lower()
    if again != "y":
        print("Goodbye, thank you and come again please!")
        break