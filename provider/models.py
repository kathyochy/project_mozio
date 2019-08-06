from django.db import models


# Create your models here.

class Provider(models.Model):

	name = models.CharField(max_length=255)
	email = models.EmailField()
	phone = models.IntegerField()
	language = models.CharField(max_length=255)
	currency = models.CharField(max_length=255)


	class Meta:
		unique_together = ['email']


	def __str__(self):
		return self.name

