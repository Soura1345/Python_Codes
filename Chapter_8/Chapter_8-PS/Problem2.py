# c/5 = (f-32)/9
# i.e c = ((f-32)/9)*5

def C_to_F(c):
    return ((9*c)/5)+32

def F_to_C(f):
    return ((f-32)*5)/9

celcius = float(input("Enter celcius: "))
print(f"The fehrenite of {celcius}°C is {round(C_to_F(celcius),2)}°F")

ferhenite  = float(input("Enter ferhenite: "))
print(f"The celcius of {ferhenite}°F is {round(F_to_C(ferhenite),2)}°C")