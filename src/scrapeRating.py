#!/usr/bin/env python3

import sys, requests, re
from bs4 import BeautifulSoup
from helper import checkValidCourse
from constants import UNIELECTIVES_URL
import math

regex = r"overallRating\\\":[0-9]"

def wilson_lower_bound(pos, n):
    if n == 0:
        return n

    z = 1.96
    phat =  float(pos) / n

    return (phat + z*z/(2*n) - z * math.sqrt((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n)


def scrapeRating(courseCode: str) -> int:
    if (not checkValidCourse(courseCode)):
        print(f"Invalid course code: {courseCode}")
        return

    try:
        html = requests.get(UNIELECTIVES_URL + courseCode)
        soup = BeautifulSoup(html.text, 'html.parser')
        return extractRating(soup)

    except:
        print({f"error : could not fetch the HTML for the course: {courseCode}"}, file=sys.stderr)
        return {f"error : could not fetch the HTML for the course: {courseCode}"}


def extractRating(soup: BeautifulSoup) -> int:
    soup_string = convertToString(soup.find("body").find_all("script")[-1])
    ratings = re.findall(regex, soup_string)
    recommended = 0
    for rating in ratings:
        int_rating = int(re.sub(r".*([0-9])", r"\1", rating))
        if int_rating >= 3:
            recommended +=1

    return wilson_lower_bound(recommended, len(ratings))


def convertToString(soup_tag) -> str:
    new_string = ""
    for tag in soup_tag:
        for char in tag:
            new_string += char
    return new_string

# if __name__ == "__main__":
#     print(scrapeRating("CRIM3020"))

