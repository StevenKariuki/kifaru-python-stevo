# 1.Withdraw
# 2.Check balance
# 3.Deposit
# 4.change pin
# 5.exit

account = {
    "name":"steven",
    "pin": 1234,
    "balance" : 500000
}
def withdraw(agent, amount, pin):
    if pin == account["pin"]:
        print("======LOGIN SUCCESSFUL=======")
        print("==============================")
        print(f'==========KARIBU (account["name])')
        print("===========WITHDRAW============")
        if amount <= account["balance"]:
            print("========APPROVED")
            print(f'Confirm you have successfully withdrawn KES (amount) from Agent No.(Agent)in westlands Nairobi')
            balance = account["balance"]
            print("your Balance is :",balance)
        else:
            print("insuficient account balance.Try Again!!!")    
            print("Your account has :", account["balance"])

    else:
        print("You Entered a wrong pin,Try Again....")        

def menu():
   while True: 
    print("Please choose an option")
    print("1.Withdraw")
    print("2.Check Balance")       
    print("3.Deposit")
    print("4.Change pin") 
    print("5.Exit")
    
    option = int(input("Enter Your Option e.g 1 for withdraw."))
    if option == 1:
        withdraw(int(input("Enter the Agent Number"))),int(input("Enter The Number:")), int(input("Enter Your pin:"))
    elif option == 5:
        break
    else:
        print("Coming Soon") 

menu()
