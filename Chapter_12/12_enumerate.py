l = [3,54,13,654,789]

# index = 0
# for item in l:
#     print(f"The item no.at index {index} is {item}")
#     index += 1

# This can be simplified by enumerate function

for index, item in enumerate(l):
    print(f"The item no.at index {index} is {item}")