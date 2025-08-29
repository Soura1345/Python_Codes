n = int(input("Enter a no. to perfoem it's table: "))

table = [n*i for i in range(1,11)]
with open("table.txt", "a") as f:
    f.write(f"Table of {n} : {str(table)} \n")