#John Newberry
#2/11/2014
#Rev exercise 4
Range = True
while Range == True:
    number = int(input("Please enter a number between 10 and 20: "))
    if number < 10:
        print("The number you entered is below 10")
    elif number > 20:
        print("The number you entered is above 20")
    else:
        print("The number you entered is within the range")
        Range = False
