#admin login method
def adminLogin():
    count = 0
    while True:
        username = str(input("Enter username to login "))
        password = str(input("Enter password to login "))
        count += 1
        if count == 3:
            print("Maximum login trials, contact IT for authorization")
            break

        else:
            if username == "admin" and password == "Princey1.":
                print("Login successful, Welcome to ticket reservation app")
                break
                
            else:
                print("Wrong login details, please try again")
                
adminLogin()



    