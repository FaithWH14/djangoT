from django.db import models
import datetime

# Create your models here.

class jobApplication(models.Model):
    qual_choice = [
        ("NA", "NA"),
        ("SPM", "Sijil Pelajaran Malaysia"),
        ("Diploma", "Diploma"),
        ("Bachelor", "Bachelor Degree"),
        ("Master", "Master Degree"),
        ("PhD", "Doctor Degree")
    ]

    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    qualification = models.CharField(max_length = 20, choices = qual_choice, default = "NA")
    CGPA = models.DecimalField(max_digits = 3, decimal_places= 2, default=0)
    position = models.CharField(max_length = 30)
    working_experience = models.DecimalField(decimal_places = 1, max_digits = 3)
    application_date = models.DateField(auto_now_add = True)