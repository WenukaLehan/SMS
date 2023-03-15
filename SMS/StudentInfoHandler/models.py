from django.db import models
from GuardianInfoHandler.models import GuardianInfo


class StudentInfo(models.Model):
    index_number = models.IntegerField(primary_key=True, unique=True)
    full_name = models.CharField(max_length=255)
    name_with_initials = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    enrolled_date = models.DateField(auto_now=True)
    address = models.TextField()
    alumni_status = models.BooleanField(default=False) # For alumni this will become True
    special_notes = models.JSONField()
    class_info = models.CharField(max_length=10)
    RFID_key = models.CharField(max_length=25)
    Guardian = models.ForeignKey(
        GuardianInfo, on_delete=models.CASCADE
    )
    
class ParentInfo(models.Model):
    student_index_number = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    mother_name = models.CharField(max_length=255)
    mother_status = models.CharField(max_length=10) 
    mother_special_notes = models.JSONField()
    father_name = models.CharField(max_length=255)
    father_status = models.CharField(max_length=10)
    father_special_notes = models.JSONField()