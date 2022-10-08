from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Thing(models.Model):
 name=models.CharField(max_length=30,blank=False,unique=True)
 description=models.CharField(max_length=120,blank=True,unique=False)
 quantity=models.BigIntegerField(unique=False)

