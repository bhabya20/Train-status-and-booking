class Train:
    def __init__(self, name, fare, seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print("*******************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("*******************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs{self.fare}")


    def bookTicket(self):
       if len(self.seats) > 0:
          print(f"Your ticket has been booked! Your seat number is {self.seats}")
          self.seats.pop()
       else:
          print("Sorry the train is full! Kindly try in tatkal")


    def cancelTicket(self,seatNo):
        self.seatNo=seatNo
        self.seats.append(seatNo)
        print(f"Your seat is cancelled:{self.seatNo}")
         
intercity = Train("Intercity Express: 14015", 90, [1,2,3,4])
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket(4)
intercity.getStatus()
