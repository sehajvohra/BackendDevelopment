from django.urls import path
from students import views

urlpatterns = [
    path('health/', views.health_check, name='health-check'),
]