# FUNCTION; is a block of code that executes only when it is called/referenced.
# Code reusability:When a developer creates a single block code,then call it anywhere in the program when it is needed,   to perfom a specific 

# Function has 2 categories:
# 1.Inbuilt Function: A function that is already existing when  python is download ,the developer only uses them,e.g print (), input (),range(), range(), int()....
print("hi there!!!")

# 2.Programmer Specific/user-defined: The programmer creats a fuction for a specific purpose e,e Mpesa payment,and then call the function only when needed.
# a).Create 
# b).Code the function logic on the body
# c).Call the body
# d).Modules

# create syntax: def function name():
#                       function body 
# NB:The function name follows the naming guideline

# create a function ta add two number


def add():
    number1 = int(input("Enter First number:"))
    number2 = int(input("Enter second number"))
    sum =  number1 + number2
    print("Answer is:",sum)
    

# call the function
# exit the function 
# syntax: function name()

#create a function to calculate simple interest

def interest():
    principal = int(input("Enter your principal:"))
    rate = int(input("Enter your rate:"))
    time = int(input("Enter your time:"))
    total = principal * rate * time
    print("Your interest is", total)

interest()    


# BMI

def calculateBmi():
    weight = 60
    height = 1.7

    bmi = weight / (height * height)
    print("Your BMI is ",Bmi)

calculateBmi()
