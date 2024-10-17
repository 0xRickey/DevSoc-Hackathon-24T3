//import data from './sampleData.json' assert { type: 'json' };
import data from './sampleData.json';

const dataBase = data["data"];

const toCourseObj = (str) => {
    return {"name": str};
}

// get all the comp courses
const getAllCourses = () => {
    let courses = [];
    for (const courseObj of dataBase) {
        for (const core of courseObj["core_courses"]) {
            if (!courses.includes(core["course_code"])) {
                courses.push(core["course_code"]);
            }
        }

        for (const pre of courseObj["prescribed_electives"]) {
            if (!courses.includes(pre["course_code"])) {
                courses.push(pre["course_code"]);
            }
        }

        for (const ge of courseObj["general_electives"]) {
            if (!courses.includes(ge["course_code"])) {
                courses.push(ge["course_code"]);
            }
        }
    }

    return courses.map(str => toCourseObj(str));
}

// get required specialisation
const specialisation = (major) => dataBase.filter(specialise => specialise["specialisation"] === major)[0];

// get all courses that are offered in the given term
// return an object:
// key: coreCourses -> array(courseInfo)
// key: prescribedCourses -> array(courseInfo)
// key: generalElectives -> array(courseInfo)
const getTermCourses = (major, term) => {
    const majorInfo = specialisation(major);

    let coreCourses = [];
    let prescribedCourses = [];
    let generalElectives = [];
    
    coreCourses = majorInfo["core_courses"].filter(core => core["terms"].includes(term));
    prescribedCourses = majorInfo["prescribed_electives"].filter(core => core["terms"].includes(term));
    generalElectives = majorInfo["general_electives"].filter(core => core["terms"].includes(term));
    
    return {
        coreCourses,
        prescribedCourses,
        generalElectives
    };
}

// remove the courses that the user did already
// ASSUMPTION: coursesDid = array(string), eg: ['COMP1511', 'COMP1521', 'COMP1221']
const removeDone = (major, term, coursesDid) => {
    const info = getTermCourses(major, term);

    if (info && info["coreCourses"]) {
        info["coreCourses"] = info["coreCourses"].filter(course => !coursesDid.includes(course["course_code"]));
    }
    if (info && info["prescribedCourses"]) {
        info["prescribedCourses"] = info["prescribedCourses"].filter(course => !coursesDid.includes(course["course_code"]));
    }
    if (info && info["generalElectives"]) {
        info["generalElectives"] = info["generalElectives"].filter(course => !coursesDid.includes(course["course_code"]));
    }

    return info;
}

const toObj = (strArray) => {
    return {"pr": strArray};
}

const modification = (prereqStr) => prereqStr.map(str => toObj(str.match(/\b[A-Z]{4}\d{4}\b/g)))

const idkWutToCall = (course) => {
    course["prereq"] = modification(course["prereq"]);

    return course;
}


const isSatisfied = (prereqs, coursesDid) => {
    if (prereqs.length === 0 ) {
        return true;
    }
    return coursesDid.filter(course => prereqs.filter(prObj =>  Array.isArray(prObj["pr"]) && prObj["pr"].includes(course)).length != 0).length == prereqs.length;
}

// prerequisite filtration
// get rid of all the courses that they did so far
// inside the database, modify the prereq[string] into prereq[{pr: [string], [string]}]
// however, we don't record students' mark, we could not see if the student's mark is enough for getting into a course that requires some wam/marks
// ASSUMPTION: course code is in the format /\b[A-Z]{4}\d{4}\b/g
// ["COMP1927 or COMP2521", "MATH1081"] => [{pr: ['COMP1927', 'COMP2521']}, {pr: ['MATH1081']}]
// ["COMP2521 or COMP1927, and a WAM of at least 70"] => [{pr: ['COMP2521', 'COMP1927']}]
const getSatisfiedPrereq = (major, term, coursesDidObj) => {
    const coursesDid = coursesDidObj.map(obj => obj["name"]);
    let list = [];
    const undoCourses = removeDone(major, term, coursesDid);

    // modification of prereq[string]
    undoCourses["coreCourses"] = undoCourses["coreCourses"].map(course => idkWutToCall(course));
    undoCourses["prescribedCourses"] = undoCourses["prescribedCourses"].map(course => idkWutToCall(course));
    undoCourses["generalElectives"] = undoCourses["generalElectives"].map(course => idkWutToCall(course));

    // get courses that student can do
    undoCourses["coreCourses"] = undoCourses["coreCourses"].filter(course => isSatisfied(course["prereq"], coursesDid));
    undoCourses["prescribedCourses"] = undoCourses["prescribedCourses"].filter(course => isSatisfied(course["prereq"], coursesDid));
    undoCourses["generalElectives"] = undoCourses["generalElectives"].filter(course => isSatisfied(course["prereq"], coursesDid));

    for (const course of undoCourses["coreCourses"]) {
        list.push({
            code: course["course_code"],
            handbookUrl: course["handbook_link"]
        });
    }

    for (const course of undoCourses["prescribedCourses"]) {
        list.push({
            code: course["course_code"],
            handbookUrl: course["handbook_link"]
        });
    }

    for (const course of undoCourses["generalElectives"]) {
        list.push({
            code: course["course_code"],
            handbookUrl: course["handbook_link"]
        });
    }

    return list;
}

const getSatisfiedPrereqq = (major, term) => {
    const courses = getTermCourses(major, term);
    let list = [];

    for (const course of courses["coreCourses"]) {
        list.push({
            code: course["course_code"],
            handbookUrl: course["handbook_link"]
        });
    }

    for (const course of courses["prescribedCourses"]) {
        list.push({
            code: course["course_code"],
            handbookUrl: course["handbook_link"]
        });
    }

    for (const course of courses["generalElectives"]) {
        list.push({
            code: course["course_code"],
            handbookUrl: course["handbook_link"]
        });
    }

    return list;
}

const getCoreCourses = (major) => {
    const majorInfo = specialisation(major);
    
    let coreCourses = majorInfo["core_courses"];
   
    let list = [];

    for (const course of coreCourses) {
        list.push({
            code: course["course_code"],
            handbookUrl: course["handbook_link"],
            rating: course["rating"]
        });
    }

    return list;
};

const getElectiveCourses = (major) => {
    const majorInfo = specialisation(major);

    let prescribedCourses = majorInfo["prescribed_electives"];
    let generalElectives = majorInfo["general_electives"];
    let list = [];

    for (const course of prescribedCourses) {
        list.push({
            code: course["course_code"],
            handbookUrl: course["handbook_link"],
            rating: course["rating"]
        });
    }

    for (const course of generalElectives) {
        list.push({
            code: course["course_code"],
            handbookUrl: course["handbook_link"],
            rating: course["rating"]
        });
    }

    return list;
};

export { getElectiveCourses, getCoreCourses, getSatisfiedPrereq, getAllCourses, getSatisfiedPrereqq };