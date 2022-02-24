# This program reads in numbers until
# the user enters 0
# it will then print back out again
# and their average

# Author: Tosin Araba

numbers = []

# first number then we check if it is 0 in the while loop

number = int(input("enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    # read the next number and check if it is 0
    number = int(input("enter another (0 to quit): "))

for value in numbers:
    print (value)

# I want average to be a float
average = float(sum(numbers)) / len (numbers)
print ("The average number is {}".format(average))
