from django.db import models

# Create your models here.
class Post(models.Model):
	name = models.CharField(max_length=120, blank=True, null=True)