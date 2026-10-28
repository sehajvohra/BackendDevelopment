
from django.contrib import admin
from django.urls import path

from students import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", views.health_check, name="health-check"),
    path("students/", views.student_list, name="student-list"),
    path(
        "students/<int:student_id>/",
        views.student_detail,
        name="student-detail"
    ),
]
