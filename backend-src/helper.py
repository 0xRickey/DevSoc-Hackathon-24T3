#!/usr/bin/env python3

import sys, json, re

def checkValidCourse(courseCode: str) -> bool:
    courseCodeRegex = r"[A-Z]{4}[0-9]{4}"
    if (re.fullmatch(courseCodeRegex, courseCode) == None):
        return False
    else:
        return True

def extractTerms(terms: str) -> list:
    filtered_terms = []
    if len(terms) == 0:
        return filtered_terms
    terms_list = terms.strip('{').strip('}').split(',')
    for term in terms_list:
        match(term):
            case "T1":
                filtered_terms.append("1")
            case "T2":
                filtered_terms.append("2")
            case "T3":
                filtered_terms.append("3")
            case _:
                continue
    return filtered_terms