# an employee class
# Author: Tosin Araba

import datetime as dt
from Timesheetentry import *

class Employee:
    timesheets = []

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __str__(self):
        return self.first + ' ' +  self.last
