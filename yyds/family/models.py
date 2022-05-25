from django.db import models

# Create your models here.

class familyINFO(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    salary = models.DecimalField(decimal_places = 2, max_digits = 10)
    relationship = models.CharField(max_length = 10)