from django.urls import path
from students import views

urlpatterns = [
    path(
        'students/<int:student_id>/',
        views.student_detail,
        name='student-detail'
    ),
]