from django.urls import path
from drf_app import views


urlpatterns = [
    path("student_api", views.student_api),
    path("student_api/<int:id>", views.student_api_detail)
]
