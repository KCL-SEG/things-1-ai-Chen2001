from enum import unique
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


# Create your models here.
class Thing(models.Model):
 name=models.CharField(max_length=30,blank=False,unique=True)
 description=models.CharField(max_length=120,blank=True,unique=False)
 quantity=models.BigIntegerField(unique=False,validators=[MaxValueValidator(100),MinValueValidator(0)])

