#variables
#data types : strings (str), integers(int), float, lists:tuples-index,dict-key,booleans


#Control flow/control structures:The way codes/block are excuted on the program
#1.Sequential control flow :Execution is done line by line(default)
#no indentation

# name = input("Enter Name:")
# location = input("Enter Location:")

#2.Conditional control Flow 
#if, else, elif

#3.Interative Flow/Looping
#For,while


#CONDITIONAL/DECISIONS
#booleans:A data type having 2 instances:True,False
#comparision operaters:check a rellationship btn one and another(>,<, ==, !=, >=, <=)booleans are always returned
#logical operators:checks for relationships with more condition (and, or, not)

#comperisons
number1 = 10
number2 = 20
number3 = 10

print(number1 > number2)
print(number1 < number2)
print(number1 == number2)
print(number1 != number2)
print(number1 >=number2)
print(number1 <= number2)

 #logical:
 # and ->return True when BOTH conditons are true
# or -> returs true when atleast 1 condition is true
# not -> Returns the opposite of condition

print((number1>number2) or (number1==number3))
print(not(number1==number3))