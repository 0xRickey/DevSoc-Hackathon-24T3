import {
  COURSE_API,
  HANDBOOK_SEARCH,
  UNIELECTIVES_URL,
  query
} from "./constant.js";

async function getCourseInfo() {
    const result = await fetch(COURSE_API, {
        method: 'POST',
        body: JSON.stringify({
        query,
        }),
    });
    return await result.json();
}

getCourseInfo()
  .then(({ data, errors }) => {
    if (errors) {
      console.error(errors);
    }
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });

