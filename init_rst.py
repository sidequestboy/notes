#! /usr/bin/env python
from time import strftime
import datetime
from sh import touch
import os
from math import ceil

day_of_week = {0: "Monday",
               1: "Tuesday",
               2: "Wednesday",
               3: "Thursday",
               4: "Friday",
               5: "Saturday",
               6: "Sunday"
               }

schedule = {"Monday": ["CISC333", "CMPE365", "MTHE474", "MTHE326", "MTHE455"],
            "Tuesday": ["ELEC377", "MTHE494", "MTHE474", "MTHE326"],
            "Wednesday": ["CISC333", "CMPE365", "ELEC377", "MTHE455"],
            "Thursday": ["ELEC377", "CISC333", "MTHE494", "MTHE474",
                         "MTHE493", "MTHE326"],
            "Friday": ["CMPE365", "ELEC377", "MTHE494", "MTHE455"],
            "Saturday": [],
            "Sunday": [],
            }

ignore = ["CISC333", "ELEC377", "MTHE493", "MTHE494"]


def lecture_day(date_):
    week = int((date_ - datetime.datetime(2013,9,9)).days / 7 + 1)
    day = int(((date_ - datetime.datetime(2013,9,9)).days + 1) % 7)
    return (week, day)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Touch the notes files based on class schedule")
    parser.add_argument("--days", dest="days", type=int, nargs=1,
                        help="number of days to touch in the past",
                        default=[1])
    parser.add_argument("--all", dest="all", type=bool, nargs=1,
                        help="touch all files since September 2013",
                        default=False)
    parser.add_argument("--show-missing", dest="show_missing", type=bool,
                        nargs=1, help="Show days where missing notes",
                        default=False)
    parser.add_argument("--no-touch", dest="no_touch", type=bool, nargs=1,
                        help="Do not touch files", default=False)

    args = parser.parse_args()

    today = datetime.datetime.today()

    day_length = datetime.timedelta(days=1)

    if args.all:
        print("Got all argument")
        days = (today - datetime.datetime(2013, 9, 9)).days + 1
    else:
        days = args.days[0]

    for day in range(days):
        for course in schedule[day_of_week[today.weekday()]]:
            p = course + "/" + strftime("%Y-%m-%d.rst", today.timetuple())
            if course not in ignore and args.no_touch is False:
                print("touching course: {}".format(course))
                print(p)
                touch(p)
            if args.show_missing:
                if os.path.isfile(p) and os.path.getsize(p) == 0:
                    # print("Missing: {}/".format(p))
                    l_day = lecture_day(today)
                    print("\t(Week {}, Lecture {} - {})".format(l_day[0], l_day[1], course))

        today -= day_length


