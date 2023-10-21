from django.db import models
from students.models import StudentInfo
# Create your models here.
class ParentsInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    ph_no = models.CharField(max_length=20)

class StudentParent(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    parent = models.ForeignKey(ParentsInfo, on_delete=models.CASCADE)

class DailyReport(models.Model):
    Student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField()
    parent = models.ForeignKey(ParentsInfo, on_delete=models.CASCADE)
class Notification(models.Model):
    message = models.TextField()
    parent = models.ForeignKey(ParentsInfo, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)