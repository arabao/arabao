# TimesheetEntry 
# for storing infomation about timesheet entries
# Author: Tosin Araba

import datetime as dt

class Timesheetentry:

    def __init__(self,project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration

    def __str__(self):
        return self.project +':' + str(self.duration)

if __name__ == '__main__':
    test = Timesheetentry('test',dt.datetime(2021,3,19,16,20), 60)
    print (test)
    