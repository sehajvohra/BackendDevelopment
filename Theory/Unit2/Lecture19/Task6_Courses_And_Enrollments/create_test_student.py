
from database import SessionLocal
from models import Student

db = SessionLocal()

try:
    existing = db.query(Student).filter(
        Student.email == "sehaj.task6@upes.ac.in"
    ).first()

    if existing:
        print("Test student already exists")
        print("Student ID:", existing.id)
    else:
        student = Student(
            name="Sehaj Vohra",
            email="sehaj.task6@upes.ac.in",
            branch="CSE"
        )

        db.add(student)
        db.commit()
        db.refresh(student)

        print("Student created successfully")
        print("Student ID:", student.id)

finally:
    db.close()
