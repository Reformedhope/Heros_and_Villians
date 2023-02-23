from django.db import models

class Supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catch_phrase = models.CharField(max_length=255)
    


# Create your models here.
