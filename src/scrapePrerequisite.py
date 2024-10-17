#!/usr/bin/env python3

import sys
import re
import json
import requests
from bs4 import BeautifulSoup
from helper import checkValidCourse

def extractPrerequisites(soup: BeautifulSoup) -> list:
    jsonString = soup.find("script", id="__NEXT_DATA__", type="application/json").text
    jsonObject = json.loads(jsonString)
    jsonStringConverted = json.dumps(jsonObject)
    
    regexPattern = r"(?<=Prerequisite: )[a-zA-Z0-9 ()]+"
    prerequisitesList = re.findall(regexPattern, jsonStringConverted)
    return prerequisitesList

def scrapePrerequisites(courseCode: str) -> list:
    if (checkValidCourse(courseCode) == False):
        print(f"Invalid course code: {courseCode}")
        return
    
    try:
        handbookLink = f"https://www.handbook.unsw.edu.au/undergraduate/courses/2025/{courseCode}?year=2025"
        headers = {'Accept-Encoding': 'identity'}
        html = requests.get(handbookLink)
        soup = BeautifulSoup(html.text, 'html.parser')
    except:
        print(f"There was an error fetching the HTML for the course: {courseCode}")
    
    return extractPrerequisites(soup)

if __name__ == "__main__":
    print(scrapePrerequisites("COMP6080"))