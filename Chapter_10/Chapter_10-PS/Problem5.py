from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train no. {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fair in train no: {self.trainNo} from {fro} to {to} is {randint(222,555)}")

t = Train(randint(11111,99999))

t.book("Tarakeswar", "Howrah")
t.getStatus()
t.getFare("Tarakeswar", "Howrah")