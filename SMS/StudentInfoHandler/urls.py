from django.urls import path
from .views import StudentView, StudentInfoView

urlpatterns = [
    path("add/", StudentView.as_view(), name="StudentView"),
    path("<index_number:int>", StudentInfoView.as_view(), name="StudentInfoView")
]
