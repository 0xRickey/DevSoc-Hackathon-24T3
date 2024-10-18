#!/usr/bin/env python3

import json, time
from scrapeSpecialisations import scrapeSpecialisation
from constants import COMP_SPECIALISATIONS

def retrieveCourseInfo(courseCode: str) -> dict:
    try:
        with open("src/getData/courses_data.json", 'r') as coursesJson:
            courses = json.load(coursesJson)['data']
            for course in courses:
                if course['course_code'] == courseCode:
                    return course
    except json.JSONDecodeError as err:
        print(f"Error decoding JSON: {err}")

def buildDatabase(specialisations: list) -> dict:
    for specialisation in specialisations:
        tempSpecDict = scrapeSpecialisation(specialisation)
        newSpecialisationEntry = {
            "Degree" : tempSpecDict['Degree'],
            "specialisation" : tempSpecDict['specialisation'],
            "core_courses": [],
            "prescribed_electives": [],
            "general_electives": []
        }

        for courseCode in tempSpecDict['core_course_codes']:
            courseInfo = retrieveCourseInfo(courseCode=courseCode)
            if courseInfo != None:
                newSpecialisationEntry['core_courses'].append(courseInfo)
        
        for courseCode in tempSpecDict['prescribed_electives_codes']:
            courseInfo = retrieveCourseInfo(courseCode=courseCode)
            if courseInfo != None:
                newSpecialisationEntry['prescribed_electives'].append(courseInfo)

        for courseCode in tempSpecDict['general_electives_codes']:
            courseInfo = retrieveCourseInfo(courseCode=courseCode)
            if courseInfo != None:
                newSpecialisationEntry['general_electives'].append(courseInfo)

        try:
            specialisationsDb = None
            with open('src/getData/specialisation_data.json', 'r') as specialisationDbJsonFile:
                specialisationsDb = json.load(specialisationDbJsonFile)
            
            specialisationsDb['data'].append(newSpecialisationEntry)
            
            with open('src/getData/specialisation_data.json', 'w') as specialisationDbJsonFile:
                json.dump(specialisationsDb, specialisationDbJsonFile, indent=4)

        except json.JSONDecodeError as err:
            print(f"There a JSONDecodeErorr: {err}")

if __name__ == "__main__":
    buildDatabase(COMP_SPECIALISATIONS)