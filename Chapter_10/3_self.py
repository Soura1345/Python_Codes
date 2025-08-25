class Employee:
    language = "Python" # This is a class attributes
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


harry = Employee()
# harry.language = "JavaScript" # This is an instance attributes
harry.getInfo()
harry.greet()
# Employee.getInfo(harry)