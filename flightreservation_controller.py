#flight details method

def flight_details():
    sqlairflightquery = "INSERT INTO flight(fligghtdate,destination,arrivedate,price) VALUES(%s,%s,%s,%s)"
    fligghtdate = input("Enter flight depature date in format: YYYY-MM-DD: ") 
    destination = input("Enter flight destination: ")
    arrivedate = input("Enter flight destination date in format: YYYY-MM-DD: ")
    price = input("Enter flight price: ")
    insertValues = (fligghtdate,destination,arrivedate,price)
    mypointer.execute(sqlairflightquery,insertValues,)
    mydatabase.commit()
    print("Plane details successfully captured")
flight_details()


