

import csv

class Admin:
    def __init__(self):
        self.username = None
        self.password = None

    def adminRegistration(self):
        
        print()
        with open("adminCredential.csv", 'w', newline="") as f:
            w = csv.writer(f)
            self.username = input("enter username")
            self.password = input("enter password")
            w.writerow([self.username, self.password])
            print(" sucess")
        print()
     

    def adminLogin(self):
        actList = []

        with open("adminCredential.csv", 'r+', newline="") as f:
            r = csv.reader(f)
            data = list(r)
            for i in data:
                for j in i:
                    actList.append(j)

        while True:
           
            print()
            self.username = input("enter username ")
            self.password = input("enter password ")
            if self.username == str(actList[0]) and self.password == str(actList[1]):
                print()
                print("ssucess")
                break
            else:
                print("Enter correct value")
            print()
            
    ##################################################
class PassengerRegistration:

    def __init__(self):
        self.busType = None
        self.bookingList = None
        self.dl = None
        self.passengerName = None
        self.noOfPassenger = None
        self.departureLocation = None
        self.destinationLocation = None
        self.ddmmyyyy = None
        self.seatNo = None
        self.selectBusType = None
        self.busFare = None
        self.autoInc = 1
        self.countcol = 0

    def getPassengerInfo(self):
        self.passengerName = input("enter name")
        self.noOfPassenger = int(input("enter number"))
        print("1-gaza1")
        print("2-jerusalem")
        print("3-jericho")
        print("4-namblus")

        self.dl = int(input("select location"))
        if self.dl == 1:
            self.departureLocation = "gaza"
        elif self.dl == 2:
            self.departureLocation = "jerusalem"
        elif self.dl == 3:
            self.departureLocation = "jericho"
        elif self.dl == 4:
            self.departureLocation = "nablus"
        else:
            print("False")

        self.ddmmyyyy = input("enter date")  

        print("1-2-3-4-5-6-7-8-9-10")
        print("11-12-13-14-15-16-17-18-19-20")
        print("21-22-23-24-25-26-27-28-29-30")
        seatNoList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                      28, 29, 30]
        self.bookingList = []
        while True:
            self.seatNo = int(input("select seat number"))
            if self.seatNo <= 30:

                if self.seatNo in seatNoList:
                    self.bookingList.append(self.seatNo)
                    del seatNoList[self.seatNo + 1]
                    count = len(seatNoList)
                else:
                    print("allready booked")
                print("do you want to book more(y/n)")
                y = input("")
                if y == "Yes":
                    pass
                else:
                    break

            else:
                print("not available")

        print(" 1-ac =70 fare")
        print(" 2-not ac= 50fare")
        self.busType = int(input("select type"))

        if self.busType == 1:
            self.selectBusType = "ac"
            self.busFare = self.noOfPassenger * 70
        elif self.busType == 2:
            self.selectBusType = "NON AC BUS"
            self.busFare = self.noOfPassenger * 50


class PassengerDataCsv(PassengerRegistration):
    def saveInfo(self):
        try:
            with open("passengerData.csv", 'r+', newline="") as f:
                r = csv.reader(f)
                data = list(r)
                # print(self.data)
                for i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countcol += 1
                    print()
                print("it is found", self.autoInc)

        except:
            print("not available")
        finally:
            with open("passengerData.csv", 'a+', newline="") as f:
                w = csv.writer(f)
                w.writerow([self.autoInc, self.passengerName, self.noOfPassenger, self.departureLocation,
                            self.destinationLocation, self.ddmmyyyy, self.bookingList, self.selectBusType,
                            self.busFare])
                print("Save successfully")
                print()
                
#############################################################
def ticketShow():
    bln = []
    with open("passengerData.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
        id = int(input("Enter Your Booking Id  :"))
        for i in data:
            if id == int(i[0]):
                for j in i:
                    bln.append(j)
                break
    
    
    print( bln[3], bln[4],bln[0])
  
    print(bln[1], bln[2])
 
    print( bln[5] ,  bln[6])
    print(bln[7])
    print( bln[8])
  
    

class TicketShow:
    pass
########################################################
global ch



def start():  
    print("1. Admin Registration :")
    print("2. Admin Login        :")
    print()
    adminObj = Admin()
    ch = int(input("Choose Correct option :"))

    if ch != 1:
        pass
    else:
        adminObj.adminRegistration()

    if ch == 2:

        adminObj.adminLogin()

        print()
        print("1-Passenger Registration ")
        print("2-Show Ticket ")
        print()
        ch = int(input("select option"))
        if ch == 1:
            pd_obj = PassengerDataCsv()
            pd_obj.getPassengerInfo()
            pd_obj.saveInfo()
        elif ch == 2:
            obj = TicketShow()
            ticketShow()


start()