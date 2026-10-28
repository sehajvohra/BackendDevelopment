
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Student


def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)


def student_list(request):
    students = Student.objects.all().values(
        "id",
        "name",
        "email",
        "age"
    )
    return JsonResponse({"students": list(students)}, status=200)


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    return JsonResponse({
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "age": student.age
    }, status=200)
