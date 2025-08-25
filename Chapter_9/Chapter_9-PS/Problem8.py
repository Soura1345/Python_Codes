with open("Text/this.txt") as f:
    content = f.read()

with open("Text/this_copy.txt", "w") as f:
    f.write(content)