# program that reads in a students percentage mark
# And prints out corresponding grade
# program should check that the percentage is valid

# Author: Tosin Araba

# Under 40% =>Fail
# Between 40% and 49% =>Pass
# Between 50% and 59% =>Merit 2
# Between 60% and 69% => Merit 1
# Over 70%            =>Distinction

# input is 69.5

percentage = float(input("Enter the percentage: "))
#print (percentage)

roundedPercentage = round(percentage)

# be careful with ands and ors

if roundedPercentage < 0 or roundedPercentage >100:
    # Later we will show error handling
    # This should only really throw an error
    print ("please enter a number between 0 and 100")
elif roundedPercentage < 40: # we know it is greater than 0
    print ("Fail")
elif roundedPercentage < 50: # between 40 and 49
    print ("Pass")
elif roundedPercentage < 60: # between 50 and 59
    print ("Merit1")
elif roundedPercentage < 70: # between 60 and 69
    print ("Merit2")
else: # the only option left is between 70 and 100
    print ("Distinction")
