p1 = "Make a lot of money"
p2 = "bye now"
p3 = "subscribe this"
p4 = "click me"

message = input("Enter the comment: ")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("This is a SPAM")
else:
    print("Comments is not a SPAM")