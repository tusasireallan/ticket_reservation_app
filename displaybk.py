def displaybooking():
    querybooking =("SELECT * FROM student WHERE bookingid= %s")
    dbooking = input("enter your bookingid to display your booking")
    mypointer.execute(querybooking,(dbooking,))
    mydatabase.commit()
    print("booking displayed")

displaybooking()