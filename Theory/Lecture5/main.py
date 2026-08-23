from fastapi import FastAPI, HTTPException, Query
import uvicorn
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="Course Management API",
    version="1.0.0"
)


class Course(BaseModel):
    id: int
    title: str
    credits: int
    department: str


class CourseCreate(BaseModel):
    title: str
    credits: int
    department: str


courses: List[Course] = [
    Course(
        id=1,
        title="Backend Development",
        credits=4,
        department="CSE"
    ),
    Course(
        id=2,
        title="Database Management Systems",
        credits=3,
        department="CSE"
    ),
    Course(
        id=3,
        title="Computer Networks",
        credits=4,
        department="CSE"
    )
]

next_id = 4


# GET all courses
@app.get("/courses", response_model=List[Course])
def get_courses(department: Optional[str] = Query(None)):

    if department:
        return [
            course
            for course in courses
            if course.department.upper() == department.upper()
        ]

    return courses


# GET course by ID
@app.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int):

    for course in courses:
        if course.id == course_id:
            return course

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


# POST create course
@app.post(
    "/courses",
    response_model=Course,
    status_code=201
)
def create_course(course: CourseCreate):

    global next_id

    new_course = Course(
        id=next_id,
        **course.model_dump()
    )

    courses.append(new_course)
    next_id += 1

    return new_course


# PUT update course
@app.put(
    "/courses/{course_id}",
    response_model=Course
)
def update_course(
    course_id: int,
    course: CourseCreate
):

    for i, existing_course in enumerate(courses):

        if existing_course.id == course_id:

            updated_course = Course(
                id=course_id,
                **course.model_dump()
            )

            courses[i] = updated_course

            return updated_course

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


# DELETE course
@app.delete(
    "/courses/{course_id}",
    status_code=204
)
def delete_course(course_id: int):

    for i, course in enumerate(courses):

        if course.id == course_id:

            courses.pop(i)

            return

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=5000,
        reload=True
    )