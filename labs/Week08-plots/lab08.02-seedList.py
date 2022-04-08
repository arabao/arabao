# Author: Tosin Araba

import numpy as np

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # this is so that the "random" numbers are the same each time to make it easier to debug.
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)
