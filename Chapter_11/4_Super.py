class Employee:
    def __init__(self):
        print("Constructoe of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructoe of Programmer")
    b = 2

class Maneger(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructoe of Maneger")
    c = 3

# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a ,o.b)

o = Maneger()
print(o.a,o.b,o.c)