def availableairline():
    queryairline= "INSERT INTO airline(airplanename,capacity,flightID)" VALUES(%,%,%)
    airplanename = input("enter plane name?")
    capaacity = input("enter capacity")
    flightID = int(input("enter FlightID"))
    values = (airplaneme,capacity,flightID)
    mypointer.execute(queyairline,values)
    mydatabase.commit()
availableairline()