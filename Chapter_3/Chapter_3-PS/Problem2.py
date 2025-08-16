# name = input("Enter your name: ")
# date = input("Enter the date: ")

# print(f'''Dear {name},\nYou are selected!\n{date}''')

letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>", "Sourashis").replace("<|Date|>", "10/05/2025"))