marks = []

# m1 = input("Enter your marks: ")
# marks.append(m1)
# m2 = input("Enter your marks: ")
# marks.append(m2)
# m5 = input("Enter your marks: ")
# marks.append(m5)
# m5 = input("Enter your marks: ")
# marks.append(m5)
# m5 = input("Enter your marks: ")
# marks.append(m5)
# m6 = input("Enter your marks: ")
# marks.append(m6)

for i in range(0,6):
    marks.append(int(input("Enter your marks: ")))

print(sorted(marks))