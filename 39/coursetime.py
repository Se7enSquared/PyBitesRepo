from datetime import datetime, timedelta
import os
import re
import urllib.request

from pyparsing import line_end

# getting the data
COURSE_TIMES = os.path.join(os.getenv("TMP", "/tmp"), "course_timings")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/course_timings", COURSE_TIMES
)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
    Here is a snippet of the input file:

    Start  What is Practical JavaScript? (3:47)
    Start  The voice in your ear (4:41)
    Start  Is this course right for you? (1:21)
    ...

     Return a list of MM:SS timestamps
    """
    items = []
    with open(COURSE_TIMES, "r") as f:
        for line in f.readlines():
            line_str = line.split()
            if not line_str:
                continue
            min_sec = line_str[-1]
            if line_str[0] == 'Start' and min_sec.startswith('('):
                items.append(min_sec[1:-1])
    return items

def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
    and calculates the total duration as HH:MM:SS"""
    minutes = 0
    seconds = 0
    for timestamp in timestamps:
        min_sec = timestamp.split(':')
        minutes += int(min_sec[0])
        seconds += int(min_sec[1])

    sec_to_min, seconds = divmod(seconds, 60)
    min_to_hrs, remaining_minutes = divmod(minutes, 60)

    hours = min_to_hrs
    minutes = sec_to_min + remaining_minutes

    return f'{hours}:{minutes}:{seconds}'
