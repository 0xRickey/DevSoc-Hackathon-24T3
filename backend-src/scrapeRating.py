#!/usr/bin/env python3

import sys, requests, re, math
from bs4 import BeautifulSoup
from helper import checkValidCourse
from constants import UNIELECTIVES_URL

regex = r"overallRating\\\":[0-9]"

def scrapeRating(courseCode: str) -> int:
    if (not checkValidCourse(courseCode) or "COMP" not in courseCode):
        return 0

    try:
        html = requests.get(UNIELECTIVES_URL + courseCode)
        soup = BeautifulSoup(html.text, 'html.parser')
        return extractRating(soup)

    except:
        print({f"error : could not fetch the HTML for the course: {courseCode}"}, file=sys.stderr)
        return 0


def extractRating( soup: BeautifulSoup) -> int:
    scripts = soup.select('script')
    target_script = [script for script in scripts if "overallRating" in script.text]

    recommended = 0
    sum_rating = 0

    rating_list = re.findall(regex, str(target_script))

    if len(rating_list) == 0:
        return 0

    for rating_string in rating_list:
        rating = int(re.sub(r".*([0-9])", r"\1", rating_string))

        sum_rating += rating

        if rating >= 3:
            recommended += 1

    return round((sum_rating) / len(rating_list), 1)

if __name__ == "__main__":
    print(scrapeRating("COMP1511"))
