#!/usr/bin/env python3

API_URL = "https://graphql.csesoc.app/v1/graphql"

UNIELECTIVES_URL = "https://unilectives.devsoc.app/course/"

QUERY = """
query MyQuery {
  courses {
    course_code
    course_name
    faculty
    terms
    uoc
  }
}
"""

COMP_SPECIALISATIONS = ["COMPA1", "COMPD1", "COMPI1", "COMPJ1", "COMPN1", "COMPS1", "COMPY1"]