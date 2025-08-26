class Demo:
    a = 4

o = Demo()
print(o.a) # Print the class attribute because instance attributes is not present
o.a = 0 # Instance attribut in set
print(o.a) # Print the instace attribute because instance attributes is present
print(Demo.a) # Prints the class attributes
