CREATE DATABASE ticketReservation;

use ticketReservation;

CREATE TABLE flight(
flightID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
fligghtdate DATE,
destination varchar(50),
arrivedate DATE,
price varchar(200)
);

CREATE TABLE booking(
bookingID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
cname varchar (50) NOT NULL,
cphone varchar(50) NOT NULL UNIQUE,
cemail varchar(50) NOT NULL UNIQUE,
bdate DATE,
flightID int,
flightStatus varchar(50) NOT NULL ,
FOREIGN KEY(flightID) REFERENCES flight(flightID)
);


CREATE TABLE payment(
paymentID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
paymentType varchar(50) NOT NULL,
amount varchar (50) NOT NULL,
cardnumber varchar(50),
cardholdername varchar(50),
bookingID int,
FOREIGN KEY(bookingID) REFERENCES booking(bookingID)
);

CREATE TABLE airline(
airlineID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
airplainname varchar(50) NOT NULL,
capacity varchar(50) NOT NULL,
flightID int,
FOREIGN KEY(flightID) REFERENCES flight(flightID)
);

CREATE TABLE airport(
airportID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
airportname varchar(50) NOT NULL,
country varchar(50) NOT NULL,
city varchar (50) NOT NULL,
airlineID int,
FOREIGN KEY(airlineID) REFERENCES airline(airlineID)
);

