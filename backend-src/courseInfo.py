#!/usr/bin/env python3

import sys, json
from helper import checkValidCourse
from scrapeRating import scrapeRating


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

    try:
        with open("database.json", "r") as f:
            data = json.load(f)
            for courses in data:
                if (courses["course_code"] == courseCodes):
                    ratings = scrapeRating(courses["course_code"])
                    courses["rating"] = ratings["rating"]
                    courses["wilson_rating"] = ratings["wilson_rating"]
                    return courses

            print(f"{sys.argv[0]} : error: course code available or does not exist", file=sys.stderr)
            return { "error: course code available or does not exist" }


    except:
        print(f"{sys.argv[0]} : error: database unavailable", file=sys.stderr)
        return { "error: database unavailable" }


def generateCourses(program_code : str, comepleted_courses : list[str]):
    """
    Generates recommended courses for each term

    Parameters
    ----------
    program_code : str
        Program code for any course (e.g. 1234).
    completed_courses : list[str]
        List of completed course codes (e.g. COMP****).

    Returns
    -------
    list[set]
        In the form:
        {
            course_code : str,
            course_name : str,
            prereq : list[str],
            recommended_terms : list[str],
            uoc : str,
            rating : str,
            unielectives : str,

        }
    str
        Error string if anything bad goes wrong
    """
    return { "CAUGHT: not implemented yet" }




# Uncomment this code to test function
if __name__ == "__main__":
    print(getCourseInfo("COMP1511"))