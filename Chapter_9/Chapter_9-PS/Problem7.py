with open("Text/log.txt") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if("python" in line):
        print(f"The word is present in line no. {lineNo}")
        break
    lineNo += 1

else:
    print("The word is not present in the file")