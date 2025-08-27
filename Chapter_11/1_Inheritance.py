class Employee:
    company = "ITC"
    def show(self):
        print(f"The name if the employee is {self.name} and the salary is {self.salary}")


class Programmer(Employee):
    company = "ITC Infotech"
    def showLang(self):
        print(f"The name is {self.name} and he is good at {self.language} language")


a = Employee()
b = Programmer()

print(f"{a.company}\n{b.company}")
