#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

def scrape():
    link = "https://www.handbook.unsw.edu.au/undergraduate/courses/2025/COMP3121?year=2025"
    html = requests.get(link).text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())