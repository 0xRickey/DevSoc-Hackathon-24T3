Reference for database collection.

Course Info
```javascript
[
    {
        course_code : "String",
        course_name : "String",
        prereq : "Array<String>",
        terms : "Array<String>",
        uoc : "String", // Please convert to int when calculating total uoc :)
        rating : "String", // ^
        handbook_link: "String",
        unielectives_link: "String"
    },
]
```

Degrees
```javascript
{
    [
        {
            Degree: "String",
            specialisation: "String",
            core_courses: [...], // Sorted alphabetically by name before written ()
            prescribed_electives: [...], // sorted by rating (displayed first and above general_electives)
            general_electives: [...] // sorted by rating (displayed after prescribed_electives)
        }
    ]
}
```

Example
```javascript
{
    [
        {
            Degree: "Computer Science",
            specialisation: "Artificial Intelligence",
            core_courses: 
            [
                {
                    course_code : "COMP3121",
                    course_name : "Programming Fundamentals",
                    prereq : ["COMP1927 or COMP2521", "MATHS1081"],
                    terms : ["1", "2", "3"],
                    uoc : "6", // Please convert to int when calculating total uoc :)
                    rating : "3.45",
                    handbook_link: "https://handbook.unsw.edu.au/undergraduate/courses/2025/COMP3121?year=2025",
                    unielectives_link: "https://unilectives.devsoc.app/course/COMP3121"
                }
            ],

            // prescribed_electives are sorted by rating (displayed first and above general_electives)
            prescribed_electives: [
                {
                    course_code : "COMP3431",
                    course_name : "Robotic Software Architecture",
                    prereq : ["COMP2521 or COMP1927, and a WAM of at least 70"],
                    terms : ["3"],
                    uoc : "6", // Please convert to int when calculating total uoc :)
                    rating : "3.45",
                    handbook_link: "https://handbook.unsw.edu.au/undergraduate/courses/2025/COMP3431",
                    unielectives_link: "https://unilectives.devsoc.app/course/COMP3431"
                }
            ],

            // general_electives are sorted by rating (displayed after prescribed_electives)
            general_electives: [
                {
                    course_code : "COMP3311",
                    course_name : "Database Systems",
                    prereq : ["COMP2521 or COMP1927"],
                    terms : ["1","2"],
                    uoc : "6", // Please convert to int when calculating total uoc :)
                    rating : "3.45",
                    handbook_link: "https://handbook.unsw.edu.au/undergraduate/courses/2025/COMP3311",
                    unielectives_link: "https://unilectives.devsoc.app/course/COMP3311"
                }
            ]
        }
    ]
}
```