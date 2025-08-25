words = ["Donkey","bad","gande"]

with open("Text/file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"* len(word))

with open("Text/file.txt", "w") as f:
    f.write(content)