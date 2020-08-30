from contro import *

#this is a view file which imports everything from the controller file
def mainController():
    #loginAdmin() and flightsPaid()
    #this is admin login imported from controller file(contro)
    print("Welcome to AtAirlines Ticket Reservation")
    print("=================================================================")
    print("Press 1 to log in as Admin and Capture the flights: ")
    print("Press 2 to Book the the Flight: ")
    print("Press 3 to Cancel the flight booked: ")
    print("Press 4 to Display the report for a number of booked flights: ")
    print("Press 5 to pay for a ticket: ")
    print("Press 6 to Capture AirCratts to different destinations: ")
    print("Press 7 to Capture AirPorts to different flight Destinations: ")
    print("==================================================================")
    status = int(input("Please choose the Prompts for the required Service: "))
    if status ==1 and status !=2 and status !=3 and status !=4 and status !=5 and status !=6 and status !=7 and status !=8 and status !=9:
        loginAdmin()
        recordFlight()
        exit()

    elif status ==2 and status  !=3 and status !=4 and status !=5 and status !=6 and status !=7 and status !=8 and status !=9 and status !=1:
        bookFlight()
        exit()

    elif status ==3 and status!=4 and status !=5 and status !=6 and status !=7 and status !=8 and status !=9 and status !=1 and status !=2:
        fCancel()
        exit()

    elif status ==4 and status !=5 and status !=6 and status !=7 and status !=8 and status !=9 and status !=1 and status !=2 and status !=3:
        flightReport()
        exit()

    elif status ==5 and status !=6 and status  !=7 and status !=8 and status !=9 and status !=1 and status !=2 and status !=3 and status !=4:
        payFlight()
        exit()

    elif status ==6 and status !=7 and status !=8 and status !=9 and status !=1 and status !=2 and status !=3 and status !=4 and status !=5:
        fairline()
        exit()

    elif status ==7 and status !=8 and status !=9 and status !=1 and status !=2 and status !=3 and status !=4 and status !=5 and status !=6:
        fairport()
        exit

    elif status ==8 and status !=9 and status !=1 and status !=2 and status !=3 and status !=4 and status !=5 and status !=6 and status !=7:
    #    fairport()
        exit()

    elif status ==9 and status !=1 and status !=2 and status !=3 and status !=4 and status !=5 and status !=6 and status !=7 and status !=8: 
    #    fDelete()
        exit()
    else:
        print("Sorry invalid Prompt Selection entered")
        print("Try again")
mainController()





