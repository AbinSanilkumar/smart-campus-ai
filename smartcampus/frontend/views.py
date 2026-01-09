from django.shortcuts import render
from attendance.models import Attendance
from accounts.models import StudentProfile


def dashboard(request):
    total_students = StudentProfile.objects.count()
    today_attendance = Attendance.objects.count()

    context = {
        "total_students": total_students,
        "today_attendance": today_attendance,
    }
    return render(request, "dashboard.html", context)


def camera(request):
    roll_number = ''
    if request.user.is_authenticated:
        profile = StudentProfile.objects.filter(user=request.user).first()
        if profile:
            roll_number = profile.roll_number
    return render(request, "camera.html", {"roll_number": roll_number})


def attendance_page(request):
    attendance_records = Attendance.objects.all().order_by("-date", "-time")

    context = {
        "attendance": attendance_records
    }
    return render(request, "attendance.html", context)

