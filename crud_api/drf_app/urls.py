from django.urls import path
from drf_app.views import function_based_views, class_based_views


urlpatterns = [
    # Function Based View URLS
    # path("student_api", function_based_views.student_api),
    # path("student_api/<int:id>", function_based_views.student_api_detail)


    # Class Based View URLS
    path("student_api", class_based_views.StudentAPI.as_view()),

]
