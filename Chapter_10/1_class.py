class Employee:
    language = "Python" # This is a class attributes
    salary = 1200000


harry = Employee()
harry.name = "Harry" # This is an instance attributes
print(harry.name,"->", harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name,"->", rohan.language, rohan.salary)

# Here name is instance attriutes and language and salary are the class attributer as they are directly belong to the class