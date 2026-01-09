from django.db import models
from accounts.models import StudentProfile

class ExamResult(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.FloatField()
    total_marks = models.FloatField()
    exam_date = models.DateField()

    def __str__(self):
        return f"{self.student.roll_number} - {self.subject}"
