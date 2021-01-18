from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	age = models.DurationField(default=None)
	skills = models.CharField(max_length=200, null=True)
	avatar = models.ImageField()

	def __str__(self):
		return self.name
