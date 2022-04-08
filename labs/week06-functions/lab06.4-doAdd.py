#We can now write the function doAdd(students). 

#Author: Tosin Araba

def readModules():
    return []


def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)


#test
students = []
doAdd(students)
doAdd(students)
print (students)