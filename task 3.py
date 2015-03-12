#John Newberry
#21/10/2014
#Revision task 3
numbers = int(input("Please input the number of values you want to find the average of: "))
result = 0
for count in range(numbers):
    total = int(input("Please input number: "))
    result = total + result
result = result / numbers
print(result)
