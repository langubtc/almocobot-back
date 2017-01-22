from django.db import models
from django.utils import timezone

class User(models.Model):
	userId = models.CharField(max_length=200, primary_key=True)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.userId

class Place(models.Model):
	placename = models.CharField(max_length=500)
	address = models.CharField(max_length=500, blank=True)

	def __int__(self):
		return self.id

class UserPlace(models.Model):
	userId = models.ForeignKey(User)
	placeId = models.ForeignKey(Place)
	fav = models.BooleanField()

	def __int__(self):
		return self.id