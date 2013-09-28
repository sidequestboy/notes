#! /usr/bin/env python
from time import strftime
import datetime
from sh import touch

day_of_week = {0: "Monday",
               1: "Tuesday",
               2: "Wednesday",
               3: "Thursday",
               4: "Friday",
               5: "Saturday",
               6: "Sunday"
               }

schedule = {"Monday": ["CISC333", "CMPE365", "MTHE474", "MTHE326", "MTHE455"],
            "Tuesday": ["ELEC377", "MTHE494", "MTHE474", "MTHE455", "MTHE326"],
            "Wednesday": ["CISC333", "CMPE365", "ELEC377", "MTHE455"],
            "Thursday": ["ELEC377", "CISC333", "MTHE494", "MTHE474",
                         "MTHE493", "MTHE326"],
            "Friday": ["CMPE365", "ELEC377", "MTHE494", "MTHE455"],
            "Saturday": [],
            "Sunday": [],
            }

ignore = ["CISC333", "ELEC377", "MTHE493", "MTHE494"]

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Touch the notes files based on class schedule")
    parser.add_argument("--days", dest="days", type=int, nargs=1,
                        help="number of days to touch in the past", default=[1])

    args = parser.parse_args()

    today = datetime.datetime.today()

    day_length = datetime.timedelta(days=1)

    for day in range(args.days[0]):
        for course in schedule[day_of_week[today.weekday()]]:
            print(day_of_week[today.weekday()])
            if course not in ignore:
                print("touching course: {}".format(course))
                print(course + "/" + strftime("%Y-%m-%d.rst"))
                touch(course + "/" + strftime("%Y-%m-%d.rst"))
        today -= day_length
