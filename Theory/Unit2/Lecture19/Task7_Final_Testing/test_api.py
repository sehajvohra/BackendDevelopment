
import importlib.util
import os
import sys
import tempfile
from pathlib import Path

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool


# Locate the existing Task 1 application
TASK1_PATH = (
    Path(__file__).resolve().parent.parent
    / "Task1_Project_Setup"
)

sys.path.insert(0, str(TASK1_PATH))


def load_module(module_name: str, file_name: str):
    module_path = TASK1_PATH / file_name
    spec = importlib.util.spec_from_file_location(module_name, module_path)

    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load module from {module_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


main_module = load_module("task1_main", "main.py")
database_module = load_module("task1_database", "database.py")

app = main_module.app
Base = database_module.Base
get_db = database_module.get_db


# Create a separate temporary database for testing
test_db_file = tempfile.NamedTemporaryFile(
    suffix=".db",
    delete=False
)
test_db_file.close()

TEST_DATABASE_URL = "sqlite:///" + test_db_file.name

test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine
)


# Create tables in the test database
Base.metadata.create_all(bind=test_engine)


# Connect API requests to the test database
def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


# Test 1: Create a student
def test_create_student():
    response = client.post(
        "/students",
        json={
            "id": "TEST101",
            "name": "Sehaj Vohra",
            "email": "sehaj.test@example.com",
            "branch": "CSE",
            "semester": 5
        }
    )

    assert response.status_code == 201, response.text


# Test 2: Retrieve the list of students

def test_list_students():
    response = client.get("/students")

    assert response.status_code == 200

    result = response.json()

    assert isinstance(result, dict)
    assert "data" in result
    assert "total" in result
    assert isinstance(result["data"], list)

# Test 3: Retrieve a student that does not exist

def test_student_not_found():
    response = client.get("/students/999999")

    assert response.status_code == 404

# Test 4: Reject invalid student data
def test_invalid_student_data():
    response = client.post(
        "/students",
        json={
            "id": "TEST102",
            "name": "Test Student",
            "email": "invalid-email",
            "branch": "CSE",
            "semester": 5
        }
    )

    assert response.status_code == 422


# Clean up after all tests
def teardown_module():
    app.dependency_overrides.clear()
    client.close()
    test_engine.dispose()

    if os.path.exists(test_db_file.name):
        os.remove(test_db_file.name)
