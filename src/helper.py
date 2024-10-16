#!/usr/bin/env python3

import sys, json

def getUOCCompleted(course_list: list[set]):
    """
    Gets total UOC completed

    Parameters
    ----------
    course_list : list[set]
        List of completed courses

    Returns
    -------
    int:
        Total UOC completed
    """
    return { "CAUGHT: not implemented yet" }

def getRecommendedTerms(course : set):
    """
    Returns a list of the most popular terms the course has been taken

    Parameters
    ----------
    course : set
        Course info

    Returns
    -------
    list[str]:
        List of terms
    """
    return { "CAUGHT: not implemented yet" }

def meetsPrerequisites(comepleted_courses : list[str], course : set):
    """
    Returns a list of the most popular terms the course has been taken

    Parameters
    ----------
    completed_courses : list[str]
        List of completed course codes (e.g. COMP****).
    course : set
        Course info

    Returns
    -------
    boolean
        Whether the course prerequisites have been met
    """
    return { "CAUGHT: not implemented yet" }