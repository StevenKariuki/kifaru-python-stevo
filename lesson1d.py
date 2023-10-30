#DATA TYPES:types of value stored on a variable

height =1.6 #Numeric value with some decimals - Floating Point (float)
age = 24 #Numeric value withoout decimals - Integers (int)
county = "nairobi" #sequence of characters -Strings (str)


#COMPUTATIONS: 
#write a program to add two numbers

number1 = 450 #first value stored
number2 =600 #second value stored

sum = number1 + number2
print("The answer is ",sum)

#write a program to calculate simple interest
#principle:amount deposited in a bank e, 25000
#rate:how the amount will accumulate with time e,g 4
#time :duration of the deposit e,g 5

#formula (algorithm):(p*R*T)/100
#input("message") function: request data from the user

principal = int(input("Enter Your Principal:"))
rate = int(input("Enter the Rate:"))
time = int(input("Enter the time:"))

interest =(principal * rate *time)/100
total =principal + interest
print("you accumulated", interest)
print("you accumulated ", interest)
