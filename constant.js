export const COURSE_API = "https://graphql.csesoc.app/v1/graphql";

export const HANDBOOK_SEARCH = "https://handbook.unsw.edu.au/search";

export const UNIELECTIVES_URL = "https://unilectives.devsoc.app/";

export const query = `
query MyQuery {
  courses {
    terms
    faculty
    course_name
    course_code
  }
}
`;



