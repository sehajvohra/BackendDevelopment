
from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from database import engine, get_db, Base
from models import Student, Course, Enrollment
from schemas import CourseCreate, CourseResponse
from schemas import EnrollmentCreate, EnrollmentResponse


# Create database tables if they do not exist
Base.metadata.create_all(bind=engine)


# Create the FastAPI application
app = FastAPI(
    title="Courses and Enrollments API",
    description="API for managing courses and student enrollments",
    version="1.0.0"
)


# GET: List courses with optional filters
@app.get("/courses", response_model=list[CourseResponse])
def list_courses(
    department_id: Optional[int] = Query(None),
    credits: Optional[int] = Query(None, ge=1, le=6),
    db: Session = Depends(get_db)
):
    query = db.query(Course)

    if department_id is not None:
        query = query.filter(Course.department_id == department_id)

    if credits is not None:
        query = query.filter(Course.credits == credits)

    return query.all()


# POST: Create a course
@app.post("/courses", response_model=CourseResponse, status_code=201)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(Course).filter(
        Course.id == course.id
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Course already exists"
        )

    db_course = Course(**course.model_dump())

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course


# GET: List enrollments for a student
@app.get(
    "/students/{student_id}/enrollments",
    response_model=list[EnrollmentResponse]
)
def list_student_enrollments(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return db.query(Enrollment).filter(
        Enrollment.student_id == student_id
    ).all()


# POST: Enroll a student in a course
@app.post(
    "/students/{student_id}/enrollments",
    response_model=EnrollmentResponse,
    status_code=201
)
def create_enrollment(
    student_id: int,
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    course = db.query(Course).filter(
        Course.id == enrollment.course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    existing = db.query(Enrollment).filter(
        Enrollment.student_id == student_id,
        Enrollment.course_id == enrollment.course_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Already enrolled in this course"
        )

    db_enrollment = Enrollment(
        student_id=student_id,
        **enrollment.model_dump()
    )

    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)

    return db_enrollment


# DELETE: Remove an enrollment
@app.delete(
    "/students/{student_id}/enrollments/{course_id}",
    status_code=204
)
def delete_enrollment(
    student_id: int,
    course_id: str,
    db: Session = Depends(get_db)
):
    enrollment = db.query(Enrollment).filter(
        Enrollment.student_id == student_id,
        Enrollment.course_id == course_id
    ).first()

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    db.delete(enrollment)
    db.commit()

    return None


# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
