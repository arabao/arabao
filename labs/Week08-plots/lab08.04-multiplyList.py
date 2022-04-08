# Author: Tosin Araba

import numpy as np

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10


salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)

# you can also multiply 
salariesMult = salaries * 1.05 # add 5% by mulitplying by 1.05
print(salariesMult)
# this is a float array to convert to an int array
newSalaries = salariesMult.astype(int)
print(newSalaries)
