class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Soura", 1200000, 712410)
print(p.name, p.salary, p.pin, p.company)

r = Programmer("Rohan", 1400000, 712413)
print(r.name, r.salary, r.pin, r.company)