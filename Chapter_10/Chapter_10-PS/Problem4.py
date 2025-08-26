import math

class Calculator:
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"The square of the no. is: {pow(self.n,2)}")
    
    def cube(self):
        print(f"The cube of the no. is: {pow(self.n,3)}")

    def sqRoot(self):
        print(f"The square root of the no. id: {round(math.sqrt(self.n),2)}")
    
    @staticmethod
    def hello():
        print("Hello There..!")
    
a = Calculator(int(input("Enter the no: ")))
a.square()
a.cube()
a.sqRoot()
a.hello()