import os

directory_path = '/Windows'

contents = os.listdir(directory_path)

for item in contents:
    print(item)