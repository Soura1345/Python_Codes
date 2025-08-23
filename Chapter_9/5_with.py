# f = open("Chapter_9/file.txt")
# print(f.read())
# f.close()

# The same can be written by 'with' statement

with open("Chapter_9/file.txt") as f:
    print(f.read())

# You don't have to close the file in this case