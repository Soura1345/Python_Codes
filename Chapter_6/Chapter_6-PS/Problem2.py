sub1 = int(input("Enter maths marks: "))
sub2 = int(input("Enter physics marks: "))
sub3 = int (input("Enter chenistry marks: "))

totalPercentage = ((sub1+sub2+sub3) / 3)

if(totalPercentage >= 44 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("You got", totalPercentage,"%")
    print("PASSED")
else:
    print("You got", totalPercentage,"%")
    print("FAILED")