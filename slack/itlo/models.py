from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class State(models.Model):
	state = models.CharField(max_length=5)

	def __str__(self):
		return self.state