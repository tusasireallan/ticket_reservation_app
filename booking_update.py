from fconnect import *
def updatebooking():
    queryupdate = "UPDATE booking SET email = %s WHERE bookingid = %s"
    email = input("Enter your email for update? ")
    bookingid = int(input("Enter your booking number to update your profile? "))
    values = (email,bookingid)
    dbasepointer.execute(queryupdate,values)
    conn.commit()
    print("Profile updated successfully")
updatebooking()