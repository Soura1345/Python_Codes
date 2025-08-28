class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self,value):
        return Vector(self.i + value.i, self.j + value.j, self.k + value.k)
    
    def __mul__(self,value):
        result = self.i * value.i + self.j * value.j + self.k * value.k
        return result
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
v3 = Vector(7,8,9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)

print(v1 + v2 + v3)