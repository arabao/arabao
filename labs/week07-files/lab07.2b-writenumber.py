#function that takes in a number and overwrites a file with that
#number (count.txt). test it and check that the file has been changed

#Author: Tosin Araba

filename = "count.txt"
def writeNumber(number):
    with open(filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# test it
writeNumber(3)