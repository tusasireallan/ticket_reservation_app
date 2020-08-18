
CREATE TABLE payment(paymentid int PRIMARY KEY AUTO_INCREMENT,
paymentType varchar(50) NOT NULL,
amount int(50) NOT NULL,
cardholdername varchar(50),
cardnumber varchar(50),
bookingid int,
FOREIGN key(bookingid) REFERENCEs booking(bookingid)
);

def paymentinsert():
    query = "INSERT INTO payment(paymentType,amount,cardholdername,cardnumber,bookingid) VALUES(%s,%s,%s,%s,%s)"
    paymentType = input("Enter method of payment? ")
    amount = input("Enter amount to be paid? ")
    cardholdername = input("Enter card holder name? ")
    cardnumber = int(input("Enter card number? "))
    bookingid = int(input("Enter bookingid? "))
    values = (paymentType,amount,cardholdername,cardnumber,bookingid)
    dbasepointer.execute(query,values)
    conn.commit()
    print("Data inserted ok")
paymentinsert()