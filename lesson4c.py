# conditions 
# booleans
#comparision and logical 

# if

# if coondition:
#      if:statement  
#
age = 15
if age < 18: 
    print("DONT ISSUE ID")

# if....else conditions     
password = "12345"
username = "user1"

checkName = str(input("Enter Your Username"))
if checkName == username:
    print("login successful")
else:
    print("login unsuccessful")    
check = str(input("Enter Your Password"))
if check == password and checkName == username:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

#compromise the system to access the user wirth wrong credentials


#if...else if(elif)...else: checks for multiple conditions and executes where it meets the true booleans, otherwise it excecutes the else part


#GRADING SYSTEM  
# 0-40 -> E
# 49-50 -> D
# 51-60 ->C
# 61-70 ->B
# 71-80 -> A
score = int(input("Enter your Score:" ))
if score >0 and score <= 40:
    print("Grade E")

elif score > 40 and score <= 50:
    print("Grade D")

elif score >50 and score <= 60:
    print("grade C")  

elif score >60 and score <=70:
    print("grade B")

elif score >70 and score <=100:
    print("grade A")    

else:
    print("Invalid Marks...Enter Again")        
