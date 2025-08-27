class Employee:
    company = "ITC"
    name = "Soura"
    def show(self):
        print(f"The name if the employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLang(self):
        print(f"Out of all language here is your language: {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLang(self):
        print(f"The name is {self.company} and he is good at {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLang()
b.showLang()
