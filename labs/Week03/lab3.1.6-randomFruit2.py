# This program prints out a ramdom fruit
# Using a tuple not a list
# Author: Tosin Araba

import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear')

# We want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("A Random Fruit: {} ".format(fruit))
