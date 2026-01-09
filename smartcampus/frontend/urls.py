from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", lambda request: redirect("dashboard/")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("camera/", views.camera, name="camera"),
    path("attendance/", views.attendance_page, name="attendance"),
]
