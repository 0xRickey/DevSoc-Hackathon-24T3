#!/usr/bin/env python3

import sys, os, requests, json, time

url = "https://graphql.csesoc.app/v1/graphql"

query = """
query MyQuery {
  courses {
    course_code
    course_name
    faculty
    terms
    uoc
    times {
      day
      time
      weeks
      location
    }
  }
}
"""

def generateCourseDatabase():
    if (not checkDatabaseAge()):
        return

    res = requests.post(url, json = {
        'query': query
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
                    "rating" : 0,
                    "unielectives" : "https://unilectives.devsoc.app/course/" + course["course_code"],
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
    current_time = time.time()

    last_modified = os.stat("database.json").st_mtime

    if (current_time - last_modified >= 86400 * 365):
        return True

    return False


# Uncomment this code to test function
# if __name__ == "__main__":
#     getCourseInfo()