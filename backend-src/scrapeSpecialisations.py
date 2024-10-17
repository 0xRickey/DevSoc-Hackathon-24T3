#!/usr/bin/env python3

# 1. Request html from webpage
# 2. Take page content json and turn it into a json object
# 3. Take json object and turn it into a json string
# 4. Use regex to extract the course codes of the:
#       a. core courses
#       b. discipline / prescribed courses
#       a. other related courses
# 5. Put the extracted course codes into their own lists by category
# 6. Load courses.json
# 7. use the lists extracted from the HTML to create the:
#       a. core_courses
#       a. prescribed_electives
#       a. general_electives
# arrays in the degrees.json file.

from requests_html import HTMLSession
from bs4 import BeautifulSoup

def extractCoreCourses(soup: BeautifulSoup) -> list:       
    coreCouresDiv = soup.find('div', class_="css-121k0sr-Box--Box-Box-styled--SAccordionBody e1s7etki11", id="Core Courses")
    courseCodesList = []
    if coreCouresDiv:
        courseCodeDivs = coreCouresDiv.find_all('div', class_="section1 css-n5lzii-Links--StyledAILinkHeaderSection e1t6s54p6")
        for div in courseCodeDivs:
            courseCodesList += div
        print(courseCodesList)
    else:
        print("Was not able to find the Core Coures")

    return courseCodesList

def extractPrescribedElectives():
    pass

def extractOtherElectives():
    pass

def main(specialisation: str):
    try:
        specialisationLink = f"https://handbook.unsw.edu.au/undergraduate/specialisations/2025/{specialisation}"
        session = HTMLSession()
        response = session.get(specialisationLink)
        response.html.render()
        soup = BeautifulSoup(response.html.html, "html.parser")

        coreCourses = extractCoreCourses(soup)
        # prescribedElectives = extractPrescribedElectives(soup)
        # otherRelatedElectives = extractOtherElectives(soup)
    except:
        print(f"There was an error getting HTML from {specialisationLink}")

if __name__ == "__main__":
    main("COMPI1")