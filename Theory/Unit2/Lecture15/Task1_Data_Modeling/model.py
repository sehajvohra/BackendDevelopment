from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import date

# Create SQLite database connection
engine = create_engine("sqlite:///students.db")

# Create base class for SQLAlchemy models
Base = declarative_base()


# Department model
class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    students = relationship("Student", back_populates="department")
    courses = relationship("Course", back_populates="department")


# Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    branch = Column(String(50))
    enrollment_date = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")


# Course model
class Course(Base):
    __tablename__ = "courses"

    id = Column(String(10), primary_key=True)
    title = Column(String(100), nullable=False)
    credits = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")


# Enrollment model
class Enrollment(Base):
    __tablename__ = "enrollments"

    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(String(10), ForeignKey("courses.id"), primary_key=True)
    semester = Column(String(20))
    grade = Column(String(2))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


# Create database tables
Base.metadata.create_all(engine)

print("Database tables created successfully.")


# Create database session
Session = sessionmaker(bind=engine)
session = Session()


# Find existing department or create a new one
department = session.query(Department).filter_by(
    name="Computer Science"
).first()

if not department:
    department = Department(name="Computer Science")
    session.add(department)
    session.commit()


# Find existing student or create a new one
student = session.query(Student).filter_by(
    email="sehaj@upes.ac.in"
).first()

if not student:
    student = Student(
        name="Sehaj Vohra",
        email="sehaj@upes.ac.in",
        branch="CSE",
        enrollment_date=date(2026, 10, 1),
        department_id=department.id
    )

    session.add(student)
    session.commit()

    print("Student added successfully.")
else:
    print("Student already exists.")


# Display student details
print("Student ID:", student.id)
print("Student Name:", student.name)
print("Student Branch:", student.branch)
print("Department:", student.department.name)


# READ operation
print("\nAll CSE Students:")

students = session.query(Student).filter(
    Student.branch == "CSE"
).all()

for student in students:
    print(
        student.id,
        student.name,
        student.email,
        student.branch
    )

# UPDATE operation
print("\nUPDATE Student:")

student_to_update = session.query(Student).filter_by(
    email="sehaj@upes.ac.in"
).first()

if student_to_update:
    student_to_update.branch = "ECE"
    session.commit()

    print("Student branch updated successfully.")
    print("Student Name:", student_to_update.name)
    print("New Branch:", student_to_update.branch)

# DELETE operation
print("\nDELETE Student:")

student_to_delete = session.query(Student).filter_by(
    email="sehaj@upes.ac.in"
).first()

if student_to_delete:
    session.delete(student_to_delete)
    session.commit()

    print("Student deleted successfully.")
else:
    print("Student not found.")

# Verify DELETE operation
print("\nChecking student after deletion:")

deleted_student = session.query(Student).filter_by(
    email="sehaj@upes.ac.in"
).first()

if deleted_student:
    print("Student still exists.")
else:
    print("Student not found. DELETE verified successfully.")