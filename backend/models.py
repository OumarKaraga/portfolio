from django.db import models

class User(models.Model):
	#user = models.ForeignKey(User)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=18)
	validation = models.CharField(max_length=200, default="")


