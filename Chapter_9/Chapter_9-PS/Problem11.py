with open("Text/old.txt", "r") as f:
    content = f.read()

with open("Text/rename_by_python.txt","w") as f:
    f.write(content)


    