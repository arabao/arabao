# TimesheetEntry 
# for storing infomation about timesheet entries
# Author: Tosin Araba

import datetime as dt

class Timesheetentry:

    def __init__(self,project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration
