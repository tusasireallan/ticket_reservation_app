#airline reservation method

def airline_details():
    sqlairplanequery = "INSERT INTO airline(airplainname,capacity,flightID) VALUES(%s,%s,%s)"
    airplainname = input("Enter name of airline: ")
    capacity = input("Enter airline capacity: ")
    flightID = int(input("Enter flightID: "))
    insertValues = (airplainname,capacity,flightID)
    mypointer.execute(sqlairplanequery,insertValues,)
    mydatabase.commit()
    print("Plane details successfully captured")
airline_details()
