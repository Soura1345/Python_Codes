import math

class Calculator:
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"The square of the no. is: {pow(self.n,2)}")
    
    def cube(self):
        print(f"The cube of the no. is: {pow(self.n,3)}")

    def sqRoot(self):
        print(f"The square root of the no. id: {math.sqrt(self.n)}")
    
a = Calculator(int(input("Enter the no: ")))
a.square()
a.cube()
a.sqRoot()