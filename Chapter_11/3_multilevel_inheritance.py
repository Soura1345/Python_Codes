class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Maneger(Programmer):
    c = 3

o = Employee()
print(o.a)

o = Programmer()
print(o.a ,o.b)

o = Maneger()
print(o.a,o.b,o.c)