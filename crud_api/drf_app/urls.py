from django.urls import path, include
from drf_app.views import function_based_views, class_based_views, function_based_api_view, class_based_api_view, viewset_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("studentapi", viewset_view.StudentViewSet, basename="student")


urlpatterns = [
    # Function Based View URLS
    # path("student_api", function_based_views.student_api),
    # path("student_api/<int:id>", function_based_views.student_api_detail)


    # Class Based View URLS
    # path("student_api", class_based_views.StudentAPISS.as_view()),

    # Function Based api View URLS
    # path("student_api", function_based_api_view.StudentAPI),

    # Class Based api View URLS
    # path("student_api", class_based_api_view.StudentAPI.as_view()),

    # Viewset URLS
    path("", include(router.urls)),
]
