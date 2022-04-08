#Write some code to check if the file exists. To do this we will need to import
# os.path and use the isfile() function.

#Author: Tosin Araba

import os.path
filename = "count.txt"
if not os.path.isfile(filename):
    print ("File does not exist")
    #initialise file here
   