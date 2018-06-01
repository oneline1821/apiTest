from __future__ import unicode_literals
from django.db import models
from time import gmtime, strftime

# Create your models here.

class Person(models.Model):
	nombres = models.CharField(max_length=150)
	#momento = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		
			
