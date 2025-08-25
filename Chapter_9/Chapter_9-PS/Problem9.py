with open("Text/this.txt") as f:
    content1 = f.read()

with open("Text/this_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes,these files are identical")
else:
    print("Not identical")