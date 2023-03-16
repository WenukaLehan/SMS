from django.db import models
from StudentInfoHandler.models import StudentInfo

class ClassInfo(models.Model):
    class_name = models.CharField(max_length=10)  # 8-B, 10-A
    
class SubjectInfo(models.Model):
    subject = models.CharField(max_length=50)  # English
    
class ExamInfo(models.Model):
    exam = models.CharField(max_length=10) 
    subject = models.ForeignKey(SubjectInfo, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    marks = models.IntegerField()
    

class Attendance(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)