f = open("Text/poem.txt")
content = f.read()
if("Hii" in content):
    print("The word is preent")
else:
    print("The word is not present")
f.close()