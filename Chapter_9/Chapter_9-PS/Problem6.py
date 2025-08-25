with open("Text/log.txt") as f:
    content = f.read()

if("python" in content):
    print("Python is present in the file")