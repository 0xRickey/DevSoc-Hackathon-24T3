#!/usr/bin/env python3

import sys, json, re

def checkValidCourse(courseCode: str) -> bool:
    courseCodeRegex = r"[A-Z]{4}[0-9]{4}"
    if (re.fullmatch(courseCodeRegex, courseCode) == None):
        return False
    else:
        return True