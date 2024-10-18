#!/usr/bin/env python3

import sys, os, requests, json, time
from constants import API_URL, UNIELECTIVES_URL, QUERY

def generateCourseDatabase():
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
                    "prereq" : [],
                    "terms" : course["terms"],
                    "uoc" : course["uoc"],
                    "unielectives" : UNIELECTIVES_URL + course["course_code"],
                    "handbook_link" : f"https://www.handbook.unsw.edu.au/undergraduate/courses/2025/{course['course_code']}?year=2025",
                }
                for course in data["data"]["courses"]
            ]

        # May want to create a default file path for the database if we eventually move this file to a different folder
        try:
            with open("database.json", "w") as f:
                json.dump(filtered_data, f)
        except:
            print(f"{sys.argv[0]} : error: could not generate database", file=sys.stderr)
            return { "error: could not generate database" }

    else:
        print(f"{sys.argv[0]} : error: unable to make API call : response code {res}", file=sys.stderr)
        return {f"error: unable to make API call : response code {res}" }



def checkDatabaseAge():
    if (not os.path.isfile("database.json")):
        return True

    current_time = time.time()

    last_modified = os.stat("database.json").st_mtime

    if (current_time - last_modified >= 86400 * 365):
        return True

    return False


# Uncomment this code to test function
if __name__ == "__main__":
    generateCourseDatabase()