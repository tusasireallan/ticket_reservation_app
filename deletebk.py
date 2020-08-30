def cancelbooking():
    querydelete =("SELECT * FROM student WHERE bookingid= %s")
    Bdelete = input("enter your bookingid to cancel booking")
    mypointer.execute(querydelete,(Bdelete,))
    mydatabase.commit()
    print("booking cancelled")

cancelbooking()
