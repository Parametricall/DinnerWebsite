from django.db import models


# Create your models here.

class Options(models.Model):
    dinner_name = models.CharField(max_length=240)
    dinner_ingredients = models.CharField(max_length=240)
    dinner_instructions = models.CharField(max_length=240)

    def __str__(self):
        return self.dinner_name
