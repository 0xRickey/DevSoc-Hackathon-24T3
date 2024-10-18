#!/usr/bin/env python3

import sys, os, requests, json, time, re
from constants import API_URL, UNIELECTIVES_URL, QUERY, DATABASE_PATH
from scrapeRating import scrapeRating
from helper import extractTerms

def generateCourseDatabase():
    os.chdir(os.path.dirname(__file__))
    if (not checkDatabaseAge()):
        return

    res = requests.post(API_URL, json = {
        'query': QUERY
    })

    if (res.status_code == 200):
        # pretty prints json: uncomment for debugging
        # print(json.dumps(res.json(), indent = 2))

        data = res.json()

        filtered_data = [
                {
                    "course_code" : course["course_code"],
                    "course_name" : course["course_name"],
                    "prereq" : "",
                    "terms" : extractTerms(course["terms"]),
                    "uoc" : course["uoc"],
                    "unielectives" : UNIELECTIVES_URL + course["course_code"],
                    "handbook_link" : f"https://www.handbook.unsw.edu.au/undergraduate/courses/2025/{course['course_code']}?year=2025",
                    "rating" : scrapeRating(course["course_code"])
                }
                for course in data["data"]["courses"]
            ]
        try:
            with open(DATABASE_PATH, "w") as f:
                data = {
                    "data" : filtered_data
                }
                json.dump(data, f, indent=4)
        except:
            print(f"{sys.argv[0]} : error: could not generate database", file=sys.stderr)
            return { "error: could not generate database" }

    else:
        print(f"{sys.argv[0]} : error: unable to make API call : response code {res}", file=sys.stderr)
        return {f"error: unable to make API call : response code {res}" }



def checkDatabaseAge():
    if (not os.path.isfile(DATABASE_PATH)):
        return True

    current_time = time.time()

    last_modified = os.stat(DATABASE_PATH).st_mtime

    if (current_time - last_modified >= 86400 * 365):
        return True

    return False


# Uncomment this code to test function
if __name__ == "__main__":
    generateCourseDatabase()