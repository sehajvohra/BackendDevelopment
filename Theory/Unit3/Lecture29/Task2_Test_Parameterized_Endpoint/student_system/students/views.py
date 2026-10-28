from django.http import JsonResponse


def student_detail(request, student_id):
    return JsonResponse({
        "student_id": student_id
    })