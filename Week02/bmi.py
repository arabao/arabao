# program that calculates BMI
# Author: Tosin Araba

height = input('enter height in metres: ')
weight = input('enter weight in kilograms: ')

bmi = int(weight)/ float(height) **2

bmi_convert = float(bmi)

print("your BMI count is {0}".format(bmi_convert))
