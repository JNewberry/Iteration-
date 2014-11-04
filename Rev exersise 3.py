#John Newberry
#2/11/2014
#Rev exercise 3
amount = int(input("Please input the number of integers you want averaged: "))
total = 0
for count in range(0,amount):
    number = int(input("Please enter a number: "))
    total = total + number
result = total / amount
print(result)
