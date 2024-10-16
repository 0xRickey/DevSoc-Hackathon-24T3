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
        unielectives: "String",
        handbook_link: "String"
    },
]
```

Degrees
```javascript
{
    [
        Degree: "String",
        specialisation: "String",
        core_courses: [...], // Sorted alphabetically by name before written ()
        prescribed_electives: [...], // sorted by rating (displayed first and above general_electives)
        general_electives: [...] // sorted by rating (displayed after prescribed_electives)
    ]
}
```