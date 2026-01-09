from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    face_image = models.ImageField(upload_to="faces/", null=True, blank=True)

    def __str__(self):
        return self.roll_number
