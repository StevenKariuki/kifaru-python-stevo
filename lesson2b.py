#area of a triangle inputs from the user
#hint:0.5 *(base*height)

length = int(input("Enter Your  length"))
height = int(input("Enter the  height"))

area = 0.5*(length*height)
print("area is", area)

#Body Mass Index
#receive the weight from the user
#receive the height from the user
#formular:weight/(height*height)
#weight / (heiight ** 2)

weight =int(input("Enter your weight:"))
height =int(input("Enter your height in decimals:"))

bmi =weight / (height ** 2)
print("your bmi is",bmi)