from conf import *

import random as tcode

#the app admin login method
def loginAdmin():
    count=0
    while True:
            userName = input("Welcome to AtAirlines ! \n\nUsername: ")
            password = input("Password: ")
            count += 1
            if count == 3:
                print("Maximum login trials,please contact the Admin for login authorisation ")
                break

            else:
                if userName == 'admin' and password == 'Princey1.':#this is the user name and password
                    print("Admin login Successful....")
                    break                    

                else:
                    print("Wrong login details, please try again")
                    print("maximum trial login is times two")
#loginAdmin()

def recordFlight():
    #this is a method for the admin to Capture the flights booked or reserved for departing customers
    print("Please Proceed to Capture flight details")
    print("==============================================================================================================")
    sql = "INSERT INTO flight (flightID,fligghtdate,destination,arrivedate,price )  VALUES (%s,%s,%s,%s,%s)"
    flightID = int (input("Please Enter flightID: "))
    fligghtdate = input('Please Enter flight Departure Date in YYYY-MM-DD format:')
    year,month,day = map(int, fligghtdate.split('-'))
    destination = input("Please Enter Flight Destination: ") 
    arrivedate = input('Enter flight arrival Date  in YYYY-MM-DD format: ')
    year,month,day = map(int, arrivedate.split('-'))
    price = int (input ("Please Enter the Flight Amount in Rands: "))
    values = (flightID,fligghtdate,destination,arrivedate,price)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New flight Captured successfully............................................................")
#recordFlight()

def bookFlight():
    #this is a method for a customer when he's going to use the app for booking a flight
    print("Welcome to AtAirlines flight booking Menu,Please fill in your Biodata to book the ticket..")
    print("================================================================")
    sql = "INSERT INTO booking (bookingID,cname,cphone,cemail,bdate,flightID,flightStatus)  VALUES (%s,%s,%s,%s,%s,%s,%s)"
    bookingID = int (input("Please Enter bookingID: "))
    cname = input("Please Enter your names: ") 
    cphone = int (input("Please Enter your Cell phone Number: "))
    cemail = input("Please Enter customer email address: ") 
    bdate = input('Enter flight arrival Date  in YYYY-MM-DD format: ')
    year,month,day = map(int, bdate.split('-'))
    flightID = int (input("Please Enter flightID: "))
    flightStatus = input("Please Enter the flight Status: ") 
    values = (bookingID,cname,cphone,cemail,bdate,flightID,flightStatus)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New flight Booked successfully.")
    reference = tcode.randint(20200606,20200620)
    print('Booking Code',reference)
#bookFlight()

def payFlight():
    #this method is displays payment options to the customer
    print("Welcome to AtAirlines Payment Options Menu,Please proceed and pay for the flight")
    print("======================================================================")
    sql = "INSERT INTO payment (paymentID,paymentType,amount,cardnumber,cardholdername ,bookingID)  VALUES (%s,%s,%s,%s,%s,%s)"
    paymentID = int (input("Please Enter paymentID: "))
    paymentType = input("Please Enter the payment option: ") 
    amount = int (input("Please Enter amount to pay for the flight: "))
    cardnumber = int (input("Please Enter cardnumber: ")) 
    cardholdername = input("Please Enter carholdername: ")
    bookingID = int(input("Please Enter bookingID: "))
    values = (paymentID,paymentType,amount,cardnumber,cardholdername,bookingID)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"Flight payment made successfully.")
    print('Printable ticket and proof of payment is sent to your email..................................................')
#payFlight()

def fCancel():
    #this is the method to display options for flight Cashier to make any Changes for different reasons
    print("Welcome to AtAirlines flight (Cancel) Changes Menu")
    print("==========================================================================")
    qModify = "UPDATE flight SET destination=%s,fligghtdate=%s WHERE flightID =%s"
    destination = input("Enter cancel on flight destination : ")
    fligghtdate = input("Enter customer fligghtdate: ")
    flightID = input("Enter customer flightID or Pincode to confirm the flight Changes: ")
    newModify =(destination,fligghtdate,flightID)
    mypointer.execute(qModify,newModify)
    mydatabase.commit()
    print(mypointer.rowcount,"Customer Flight Cancelled successfully......................................................")
#fCancel()

def fDelete():
    #the method for deleting aparticular flight from the flights schedule
    print("Welcome to AtAirlines flight (Delete) Changes Menu.............................................................")
    print("==============================================================================")
    sqldel=("DELETE FROM flight WHERE flightID=%s")
    qdelete =input("Enter customer flightID to delete aflight: ")
    mypointer.execute(sqldel,(qdelete,))
    mydatabase.commit()
    print("Flight  Deleted from the Schedule successfully................................................................")
#fDelete()

def flightReport():
    #this method Displays areport of the number of people  for on a particular flight.
    print("The following are the flights flying to different destinations.")
    print("===========================================================================")
    qflightReport = "SELECT * FROM  flight LIMIT 5"
    mypointer.execute(qflightReport)
    newReport=mypointer.fetchall()
    for x in newReport:
        print(x)
        print(".............................................................................................................")
#        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")

#flightReport()

def flightsPaid():
    #This method shows how many booked are paid for sofar
    print("The following have successfully paid for the flight..")
    print("=========================================================================")
    qfpaid = "SELECT * FROM  payment LIMIT 5"
    mypointer.execute(qfpaid)
    newqfpaid = mypointer.fetchall()
    for x in newqfpaid:
        print(x)
        print(".............................................................................................................")

#flightsPaid()

def fairline():
    #this is the method showing different airplanes to select
    print("Welcome to AirCrafts Menu..")
    print("===================================================================")
    sql = "INSERT INTO airline (airlineID,airplainname,capacity,flightID)  VALUES (%s,%s,%s,%s)"
    airlineID = int (input("Please Enter AirlineID: "))
    airplainname = input("Please Enter AirCraft name: ") 
    capacity = int (input("Please Enter AirCraft Capacity: "))
    flightID = int (input("Please Enter flightID attached to a particular flight: ")) 
    values = (airlineID,airplainname,capacity,flightID)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"Thank you!.")
#fairline()

def fairport():
    #this is the method showing different destination airports
    print("Welcome to Airports Menue..")
    print("========================================================================")
    sql = "INSERT INTO airport (airportID,airportname,country,city,airlineID)  VALUES (%s,%s,%s,%s,%s)"
    airportID = int (input("Please Enter AirportID to allocate an Airport to the Flight: "))
    airportname = input("Please Enter Airport name to allocate an airport to a flight: ") 
    country = input("Please Enter Airport Country name for aparticular flight destination: ")
    city = input("Please Enter Airport City of the Country of a flight destination: ")
    airlineID = int (input("Please Enter AirlineID/airCraft attached to aparticular flight: "))
    values = (airportID,airportname,country,city,airlineID)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"Thank you.")
#fairport()

