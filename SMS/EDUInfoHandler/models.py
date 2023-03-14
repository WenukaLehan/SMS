from django.db import models


class ClassInfo(models.Model):
    class_name = models.CharField(max_length=10)  # 8-B, 10-A