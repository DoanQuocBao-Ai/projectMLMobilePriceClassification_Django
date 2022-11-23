from django.db import models

# Create your models here.
class Clz(models.Model):
    name = models.CharField(max_length= 50)
    file = models.BinaryField()
    score = models.FloatField()