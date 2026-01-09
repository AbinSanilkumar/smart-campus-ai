from django.db import models
from accounts.models import StudentProfile

class StudyPlan(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    priority = models.IntegerField()  # 1 = High, 2 = Medium, 3 = Low
    recommended_hours = models.FloatField()

    def __str__(self):
        return f"{self.student.roll_number} - {self.topic}"
