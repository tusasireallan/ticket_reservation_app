CREATE TABLE booking(bookingid int PRIMARY KEY AUTO_INCREMENT,
clientname varchar(50) NOT NULL,
cphone int(30) UNIQUE NOT NULL,
caddress varchar(50),
email varchar(50) NOT NULL UNIQUE,
airport varchar(50),
tdate DATE,
flightid int,
FOREIGN KEY(flightid) REFERENCES flight(flightid)
);



def bookinginsert():
    query = "INSERT INTO booking(clientname,cphone,caddress,email,airport,tdate,flightid) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    clientname = input("Enter client name? ")
    cphone = int(input("Enter phone number? "))
    address = input("Enter address? ")
    email = input("Enter email address? ")
    airport = input("Enter airport name? ")
    tdate = input("Enter travelling date? ")
    flightid = int(input("Enter flightid? "))
    values = (clientname,cphone,address,email,airport,tdate,flightid)
    dbasepointer.execute(query,values)
    conn.commit()
    print("Data inserted ok")
bookinginsert()



