#John Newberry
#21/10/2014
#Revision Task 4
inrange = False
while inrange == False:
    number = int(input("Please enter a number between 10 and 20: "))
    if number > 20 or number < 10:
        print("The number you entered is not within the range")
    else:
        print("The number you entered is within the range")
        inrange = True
