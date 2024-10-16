#!/usr/bin/env python3

import sys
import re
import requests
from bs4 import BeautifulSoup

def checkValidCourse(courseCode: str) -> bool:
    courseCodeRegex = r"[A-Z]{4}[0-9]{4}"
    if (re.fullmatch(courseCodeRegex, courseCode) == None):
        return False
    else:
        return True

def extractPrerequisites(htmlString: str) -> list:
    prerequisiteRegex = r"(?<=Prerequisite: )[A-Z]{4}[0-9]{4}(?: or [A-Z]{4}[0-9]{4}| and [A-Z]{4}[0-9]{4})*"
    prerequisitesList = re.findall(prerequisiteRegex, htmlString)
    print(prerequisitesList)
    return prerequisitesList

def scrapePrerequisites(courseCode: str) -> str:
    if (checkValidCourse(courseCode) == False):
        print(f"Invalid course code: {courseCode}")
        return
    
    handbookLink = f"https://www.handbook.unsw.edu.au/undergraduate/courses/2025/{courseCode}?year=2025"
    try:
        html = requests.get(handbookLink).text
        soup = BeautifulSoup(html, 'html.parser')
        htmlString = soup.prettify()
    except:
        print(f"There was an error fetching the HTML for the course: {courseCode}")
    
    extractPrerequisites(htmlString)

def main():
    pass

# Uncomment this code to see html print
if __name__ == "__main__":
    htmlString = scrapePrerequisites("COMP3121")