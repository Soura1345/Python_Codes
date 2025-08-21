d = {}

for i in range(2):
    name = input("Enter friends names: ")
    lang = input("Enter languagrs: ")
    d.update({name: lang})

print(d)
