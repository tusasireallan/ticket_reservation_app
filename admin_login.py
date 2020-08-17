#admin login method
def adminLogin():
    try:
        username = str(input("Enter username to login "))
        password = str(input("Enter password to login "))
    except ValueError:
        print("For wrong input, type try once more")
        print("Thank you")
    if username == "admin" and password == "Princey1.":
        print("Login successful, Welcome to ticket reservation app")
    else:
        print("Wrong login credentials, Bye")
        exit()
