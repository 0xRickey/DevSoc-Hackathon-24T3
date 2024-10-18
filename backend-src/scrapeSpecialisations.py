#!/usr/bin/env python3

# 1. Request html from webpage
# 2. use requests_html to render the html
# 3. use beautiful soup to access the html dom and extract course codes for each category of courses
# 4. Put the extracted course codes into their own lists by category

import re, time
from requests_html import HTMLSession
from bs4 import BeautifulSoup
# from constants import COMP_SPECIALISATIONS

def extractCoreCourses(soup: BeautifulSoup) -> list:
    # 1. find the three main divs that contain all the courses within them
    coursesDivs = soup.find_all('div', class_="AccordionItem css-3m2r4d-Box--Box-Box-Card--CardBody e12hqxty1")
    
    # 2. find the div with "Core Courses" as its text
    coreCoursesDiv = None
    for div in coursesDivs:
        divText = div.find('strong').text
        if "Core Course" in divText:
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

def extractDisciplineElectives(soup: BeautifulSoup) -> list:
    # 1. find the three main divs that contain all the courses within them
    coursesDivs = soup.find_all('div', class_="AccordionItem css-3m2r4d-Box--Box-Box-Card--CardBody e12hqxty1")

    if len(coursesDivs) < 3:
        return []
    
    # 2. Get the div with "Prescribed Electives" or "Discipline Electives" as its text
    disciplineElectivesDiv = None
    for div in coursesDivs:
        divText = div.find('strong').text
        if "Discipline Electives" in divText:
            disciplineElectivesDiv = div
            break
        
        elif "Prescribed Electives" in divText:
            disciplineElectivesDiv = div
            break

    # 3. Extract all prescribed courses
    disciplineElectivesCodes = []
    divTypeA = "section1 css-n5lzii-Links--StyledAILinkHeaderSection e1t6s54p6"
    for div in disciplineElectivesDiv.find_all('div', class_=divTypeA):
        disciplineElectivesCodes.append(div.text)

    divTypeB = "StyledAILinkHeaderSection__content1 css-1nnc03b-Links--StyledAILinkHeaderSection e1t6s54p6"
    for div in disciplineElectivesDiv.find_all('div', class_=divTypeB):
        disciplineElectivesCodes.append(div.text)

    return disciplineElectivesCodes

def extractOtherElectives(soup: BeautifulSoup):
    # 1. find all the main divs that contain all the courses within them
    coursesDivs = soup.find_all('div', class_="AccordionItem css-3m2r4d-Box--Box-Box-Card--CardBody e12hqxty1")
    
    # 2. Get the div with "Prescribed Electives" or "Discipline Electives" as its text
    otherElectivesDiv = None
    for div in coursesDivs:
        divText = div.find('strong').text
        if "Discipline" not in divText and "Core Course" not in divText and "Prescribed" not in divText:
            otherElectivesDiv = div

    # 3. Extract all electives and extract all the "one of the following" ones too
    otherElectivesCourseCodes = []
    divTypeA = "section1 css-n5lzii-Links--StyledAILinkHeaderSection e1t6s54p6"
    for div in otherElectivesDiv.find_all('div', class_=divTypeA):
        otherElectivesCourseCodes.append(div.text)

    divTypeB = "StyledAILinkHeaderSection__content1 css-1nnc03b-Links--StyledAILinkHeaderSection e1t6s54p6"
    for div in otherElectivesDiv.find_all('div', class_=divTypeB):
        otherElectivesCourseCodes.append(div.text)

    return otherElectivesCourseCodes

def extractDegreeName(soup: BeautifulSoup) -> str:
    degreeName = soup.find(
        'h2',
        class_="css-g23dyo-styled--StyledHeading-ComponentHeading--ComponentHeading-styled--StyledHeading e1ixoanv9"
    ).text

    if re.search(r"\([a-zA-Z ]+\)", degreeName) != None:
        degreeName = re.search(r"[a-zA-Z ]+(?=\([a-zA-Z ]+\))", degreeName).group()

    return degreeName
    

def extractSpecialisationName(soup: BeautifulSoup) -> str:
    specialisationName = soup.find(
        'h2',
        class_="css-g23dyo-styled--StyledHeading-ComponentHeading--ComponentHeading-styled--StyledHeading e1ixoanv9"
    ).text

    if re.search(r"\([a-zA-Z ]+\)", specialisationName):
        specialisationName = re.search(r"(?<=\()[a-zA-Z ]+(?=\))", specialisationName).group()

    return specialisationName

def scrapeSpecialisation(specialisation: str):
    try:
        specialisationLink = f"https://handbook.unsw.edu.au/undergraduate/specialisations/2025/{specialisation}?year=2025"
        session = HTMLSession()
        response = session.get(specialisationLink)
        response.html.render()
        soup = BeautifulSoup(response.html.html, "html.parser")

        coreCourses = extractCoreCourses(soup)
        prescribedElectives = extractDisciplineElectives(soup)
        otherRelatedElectives = extractOtherElectives(soup)
        degreeName = extractDegreeName(soup)
        specialisationName = extractSpecialisationName(soup)

        return {
            "Degree": degreeName,
            "specialisation": specialisationName,
            "core_course_codes" : coreCourses,
            "prescribed_electives_codes" : prescribedElectives,
            "general_electives_codes" : otherRelatedElectives
        }
    except:
        print(f"There was an error getting HTML from {specialisationLink}")

if __name__ == "__main__":
    # for code in COMP_SPECIALISATIONS:
    #     print(f"Program Code: {code}")
    #     scrapeSpecialisation(code)
    #     print("")
    #     time.sleep(5)
    pass