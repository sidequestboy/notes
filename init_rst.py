#! /usr/bin/env python
from time import strftime
from sh import touch
import os

schedule = {"Monday": ["CISC333", "CMPE365", "MTHE474", "MTHE326", "MTHE455"],
            "Tuesday": ["ELEC377", "MTHE494", "MTHE474", "MTHE455", "MTHE326"],
            "Wednesday": ["CISC333", "CMPE365", "ELEC377", "MTHE455"],
            "Thursday": ["ELEC377", "CISC333", "CMPE365", "MTHE494", "MTHE474",
                         "MTHE473", "MTHE326"],
            "Friday": ["CMPE365", "ELEC377", "MTHE494", "MTHE455", "CMPE365"]}

if __name__ == '__main__':
    for course in schedule[strftime("%A")]:
        print("touching course: {}".format(course))
        print(course + "/" + strftime("%Y-%m-%d.rst"))
        touch(course + "/" + strftime("%Y-%m-%d.rst"))
