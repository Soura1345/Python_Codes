word = "Donkey"

with open("Text/file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("Text/file.txt", "w") as f:
    f.write(contentNew)