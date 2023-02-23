from django.db import models
from super_types.models import SuperType #why isnt this coming forward and acting as its class

class Supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catch_phrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE, null=True)

    


# Create your models here.
