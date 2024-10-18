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
    # 1. find the three main divs that contain all the courses within them
    coursesDivs = soup.find_all('div', class_="AccordionItem css-3m2r4d-Box--Box-Box-Card--CardBody e12hqxty1")
    
    # 2. find the div with "Core Courses" as its text
    coreCoursesDiv = None
    for div in coursesDivs:
        divText = div.find('strong').text
        if divText == "Core Courses":
            coreCoursesDiv = div

    # 3. Extract all core courses and extract all the "one of the following" ones too
    coreCourseCodes = []
    divTypeA = "section1 css-n5lzii-Links--StyledAILinkHeaderSection e1t6s54p6"
    for div in coreCoursesDiv.find_all('div', class_=divTypeA):
        coreCourseCodes.append(div.text)

    divTypeB = "StyledAILinkHeaderSection__content1 css-1nnc03b-Links--StyledAILinkHeaderSection e1t6s54p6"
    for div in coreCoursesDiv.find_all('div', class_=divTypeB):
        coreCourseCodes.append(div.text)

    return coreCourseCodes

def extractPrescribedElectives(soup: BeautifulSoup) -> list:
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