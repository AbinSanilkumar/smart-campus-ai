from django.db import models
from accounts.models import StudentProfile

class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    subject = models.CharField(max_length=100)
    status = models.BooleanField(default=True)  # Present/Absent

    def __str__(self):
        return f"{self.student.roll_number} - {self.date}"
