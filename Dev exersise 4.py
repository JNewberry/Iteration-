#John Newberry
#2/11/2014
#Dev exersise 4
count = True
total = int(input("Please input the first number in the sequence: "))
while count == True:
    next = int(input("Please enter a number for the sequence, If you want to stop inputing numbers, enter -1: "))
    if next > total:
        total = next
    elif next is -1:
        count = False
        print(total)
