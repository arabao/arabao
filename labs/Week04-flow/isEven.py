# program that asks the use to enter a number
# And tells the user if number is even or odd
# Author: Tosin Araba

number = int(input("enter an integer:"))

if (number % 2) == 0 :
    print ("{} is an even number".format(number))
else:
    print ("{} is an odd number".format(number))