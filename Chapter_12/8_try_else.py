try:
    a = int(input("Enter a no.: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I'm inside else")