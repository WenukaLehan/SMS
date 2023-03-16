from django.db import models

class GuardianInfo(models.Model):
    full_name = models.CharField(max_length=255)
    name_with_initials = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    nic = models.CharField(max_length=15)
    gender = models.CharField(max_length=1)
    job = models.CharField(max_length=50)
    Relation = models.CharField(max_length=2)
    special_notes = models.JSONField()