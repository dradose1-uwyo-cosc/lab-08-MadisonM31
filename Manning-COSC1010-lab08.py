# Madison Manning
# UWYO COSC 1010
# 11/05/2024
# Lab 08
# Lab Section: 10
# Sources, people worked with, help given to:

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 



def check_numbers(string):
    #string = input("please type a number, exit to exit")
    
    isNeg = False

    if string[0] == "-":
        isNeg = True
        string = string.replace("-", "")
        
    if "." in string:
        extra_num = string.split(".")
        if len(extra_num) == 2 and extra_num[0].isdigit() and extra_num[1].isdigit():
            if isNeg == True:
                return -1*float(string)
            else:
                return float(string)

    elif string.isdigit() == True:
        if isNeg == True:
            return -1*int(string)
        else:
            return int(string)
    
    else:
        print(f"Please enter a numeric value")
        return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def y_values(m, b, x1, x2):
    
    all_y = []

    for num in range(x1, x2+1):
        y = m*num + b
        all_y.append(y)
        if num == x2:
            return all_y

while True:
    m = input("slope, exit to quit")
    if m.lower() == "exit":
        break
    m = check_numbers(m)
    b = input("y-intercept")
    b = check_numbers(b)
    x1 = input("X lower bound")
    x1 = check_numbers(x1)
    x2 = input("X upper bound")
    x2 = check_numbers(x2)

    if m != False and b != False and x1 != False and x2 != False:
        if type(x1) == float or type(x2) == float:
            print(f"please enter whole X numbers")
        else:
            print(y_values(m, b, x1, x2))





print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def sq_root(a, b, c):
    inner_eq = (b ** 2) - (4 * a * c)
    numbers = []
    added_num = 0
    sub_num = 0
    if inner_eq < 0:
        return null
    else:
        numbers.append(((-1 * b) + (inner_eq ** 0.5)) / (2 * a))
        numbers.append(((-1 * b) - (inner_eq ** 0.5)) / (2 * a))
        return numbers

while True:
    a = input("a, exit to quit")
    if a.lower() == "exit":
        break
    a = check_numbers(a)
    b = input("b")
    b = check_numbers(b)
    c =  input("c")
    c = check_numbers(c)

    if a != False and b != False and c != False and d != False:
        