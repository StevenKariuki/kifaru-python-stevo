# BANKING SYSTEM
#aCCOUNT:{ BALANCE ,PIN .}
#PIN 

for customers in range(222):
    client = {
        "pin":1234,
        "name":"steven",
        "balance":10000
    }

    pin = int(input("Enter Your Pin: "))


    if pin == client["pin"]:
        print("Login Successful")
        print("Karibu", client["name"])

        print("=====WITHDRAW=====")
        withdraw = int(input("Enter Amount to Withdraw: "))
        if withdraw <= client["balance"]:
            print("=====status=====")
            print("confirm You have withdrawn", withdraw)
            print("confirmed you have withdrawn ", withdraw)
            balance = client["balance"] -withdraw
            print("Your balance is ", balance)
        else:
            print("insufficient A/C balance,Try again!!!")    

    else:
        print("Wrong pin Try again...")        


else:
    print("inactive")


    

