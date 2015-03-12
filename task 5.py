#John Newberry
#20/10/2014
#Task 5
result = 0
total = 0
counter = 0
while result >= 0:
    result = int(input("Please enter a number and press enter, when you are done entering numbers insert -1: "))
    counter = counter + 1
    if result >= 0:
        total = total + result
total = total % counter
print(total)
