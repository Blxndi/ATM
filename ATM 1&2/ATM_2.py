from ATM_1 import ATM 
acc = ATM("Blendi",1234,1500)

while True:
    username=input("Enter username: ")
    password=int(input("Enter password: "))
    account1=acc.login(username,password)
    if account1 == False:
        break
    if account1== True:
        while True:
            print("Please type a number to continue")
            ask3= input("""What would you like to do?
            Display (1); Deposit (2); Withdraw (3) or Exit (4)? 
            """)
            if ask3 == "1":
                acc.display()
            elif ask3 == "2":
                acc.deposit()
            elif ask3 == "3":
                acc.withdraw()
            elif ask3 == "4":
                break
            else:
                print("Not supported answer!")
    
