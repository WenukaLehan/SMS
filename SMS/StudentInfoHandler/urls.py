from django.urls import path
from .views import StudentView

urlpatterns = [
    path("add/", StudentView.as_view(), name="StudentView")
]
