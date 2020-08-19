from dbconfig import *

#airport details method
def airport_details():
    print("Welcome administrator, you are now capturing the airplane details!")
    sqlairportquery = "INSERT INTO airport(airportname,country,city,airlineID) VALUES(%s,%s,%s,%s)"
    airportname = input("Enter airport name: ")
    country = input("Enter country name: ")
    city = input("Enter name of city: "))
    airlineID = int(input("Enter airlineID as captured in the airline: "))
    insertValues = (airportname,country,city,airlineID)
    mypointer.execute(sqlairportquery,insertValues,)
    mydatabase.commit()
    print("Airport details successfully captured")
airport_details()
