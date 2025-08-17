d = {} # empty dictionary

marks = {
    "Soura": 100,
    "Soumen": 92,
    "Souvik": 95,
}

# print(marks.items())
# print(marks.keys()) # left one
# print(marks.values()) # right one
# marks.update({"Soura": 99, "Snigdha": 100})
# print(marks)

print(marks.get("Soura1")) # return None
print(marks["Soura1"]) # return error