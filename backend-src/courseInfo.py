#!/usr/bin/env python3

import sys, json, os
from helper import checkValidCourse
from constants import DATABASE_PATH

def getCourseInfo(courseCodes : str):
    """
    Gets course info from database

    Parameters
    ----------
    courseCode : str
        List of course codes for any course (e.g. COMP****).

    Returns
    -------
    list[set]
        In the form:
        {
            course_code : str,
            course_name : str,
            prereq : list[str],
            terms : list[str],
            uoc : str,
            rating : str,
            unielectives : str,
        }
    str
        Error string if anything bad goes wrong
    """
    if (not checkValidCourse(courseCodes)):
        print(f"{sys.argv[0]} : error: invalid course code", file=sys.stderr)
        return { "error: invalid course code" }
    os.chdir(os.path.dirname(__file__))
    try:
        with open(DATABASE_PATH, "r") as f:
            data = json.load(f)
            for courses in data["data"]:
                if (courses["course_code"] == courseCodes):
                    return courses

            print(f"{sys.argv[0]} : error: course code available or does not exist", file=sys.stderr)
            return { "error: course code available or does not exist" }


    except:
        print(f"{sys.argv[0]} : error: database unavailable", file=sys.stderr)
        return { "error: database unavailable" }



# Uncomment this code to test function
if __name__ == "__main__":
    print(getCourseInfo("COMP1511"))