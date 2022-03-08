# Program that puts 10 random numbers into a list (queue)
# Program then outputs all the values in the list
# then takes the numbers from the list one at a time
# prints it and the current numbers in the list

# Author: Tosin Araba

import random
queue = []
numberOfNumbers=10
rangeTo=100

for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print ("queue is {}".format(queue))

while len(queue) != 0:

   currentNumber = queue.pop(0)
   print ("current Number is {} and the queue is {} ".format(currentNumber, queue))

print ("the queue is now empty")
