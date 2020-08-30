def availableflight():
    queryinsert= "INSERT INTO flight(flightID,flightdate,destanation,arrivedate,price) VALUES(%s,%s,%s,%s,%s)"
    fightID = int(input("enter Flightid"))
    flightdate = int(input("enter Flight Date"))
    arrivedate = input("enter arrive Date")
    price = input("Enter price")
    values = (flightID,flightdate,destanation,arrivedate,price)
    mypoint.excute(queryinsert,values)
    mypointer.execute(queryinsert,values)
    mydatebase.commit()
    print("flight details succsefully entered")

availableflight()