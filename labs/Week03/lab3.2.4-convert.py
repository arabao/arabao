# program that takes in a float amount in dollars
# Returns absolute amount in cents

# Author: Tosin Araba

amountInDollars = float(input("Please enter an amount:"))
absoluteNumberInCents = abs(amountInDollars)
answer = round(absoluteNumberInCents * int(input("Enter a number:")))
print ( '{} The amount in cent is {} '.format(amountInDollars, answer))
