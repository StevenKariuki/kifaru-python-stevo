#control structures:control the code execution 
# 1. Seqential -line by line (default)
# 2.Conditional-code execution is controoled by conditons (if,else ,,if elif else)
# 3.Interative/looping -a block of code execuution is respeted based on a condition ,while

# for: range 

#print the word "thank you" 10 times 


print("===FOR===")
for message in range(10):
    print("Thank you", message)

#print no from 0 - 50
for number in range(51):
    print("", number)    


#range ()
# #start, limit, inteval(increment/decrement)
# print value from 50-100 at 10 intevals
print("===FOR===")

for value in range(50, 110, 10):
    print(value)

for value in range(20, 4, -2):
    print(value)    
    