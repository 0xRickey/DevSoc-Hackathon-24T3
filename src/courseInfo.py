#!/usr/bin/env python3

import sys, json

def getCourseInfo(courseCodes : list[str]):
    """
    Gets course info from database

    Parameters
    ----------
    courseCode : list[string]
        The course code for any course (e.g. COMP****).

    Returns
    -------
    list
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
    """
    try:
        with open("database.json", "r") as f:
            courseInfoList = []
            data = json.load(f)
            for courses in data:
                if (courses["course_code"] in courseCodes):
                    courseInfoList.append(courses)

            if (len(courseInfoList) != len(courseCodes)):
                print(f"{sys.argv[0]} : error: couse code is invalid or not available", file=sys.stderr)
                return { "error: couse code is invalid or not available" }

            return courseInfoList

    except:
        print(f"{sys.argv[0]} : error: database unavailable", file=sys.stderr)
        return { "error: database unavailable" }


# Uncomment this code to test function
# if __name__ == "__main__":
#     print(getCourseInfo({"COMP1511", "COMP2511"}))