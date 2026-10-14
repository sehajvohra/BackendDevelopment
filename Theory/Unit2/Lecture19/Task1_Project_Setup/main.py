
from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
import math

from database import engine, get_db, Base
from models import Student
from schemas import (
    StudentCreate,
    StudentUpdate,
    StudentResponse,
    StudentListResponse,
    BranchEnum
)


# Create database tables if they do not exist
Base.metadata.create_all(bind=engine)


# Create the FastAPI application
app = FastAPI(
    title="Student Management API",
    description="API for managing student records",
    version="1.0.0"
)


# GET: List students with filtering and pagination
@app.get("/students", response_model=StudentListResponse)
def list_students(
    branch: Optional[BranchEnum] = Query(None, description="Filter by branch"),
    department_id: Optional[int] = Query(None, description="Filter by department"),
    search: Optional[str] = Query(None, description="Search by name or email"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db)
):
    query = db.query(Student)

    if branch:
        query = query.filter(Student.branch == branch.value)

    if department_id:
        query = query.filter(Student.department_id == department_id)

    if search:
        query = query.filter(
            Student.name.ilike(f"%{search}%") |
            Student.email.ilike(f"%{search}%")
        )

    total = query.count()
    total_pages = math.ceil(total / limit)
    offset = (page - 1) * limit

    students = query.offset(offset).limit(limit).all()

    return {
        "data": students,
        "total": total,
        "page": page,
        "limit": limit,
        "total_pages": total_pages
    }


# GET: Retrieve one student by ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(
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

    return student


# POST: Create a new student
@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    db_student = Student(**student.model_dump())

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


# PUT: Update an existing student
@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not db_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    update_data = student.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if field == "branch" and value is not None:
            value = value.value

        setattr(db_student, field, value)

    db.commit()
    db.refresh(db_student)

    return db_student


# DELETE: Delete a student by ID
@app.delete("/students/{student_id}", status_code=204)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not db_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(db_student)
    db.commit()

    return None


# Run the application directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
