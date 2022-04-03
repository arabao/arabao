# an employee class
# Author: Tosim Araba

import datetime as dt
from Timesheetentry import *

class Employee:
    Timesheets = []

    def __init__(self, first, last):
        self.first = first
        self.last = last
