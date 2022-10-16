from django.urls import path
from .views import sendData


urlpatterns = [
    path("", sendData)
]
