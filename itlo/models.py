from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class State(models.Model):
	lab_is=(("Open!","Open"),("Close",'Close'))
	state = models.CharField(max_length=5, choices=lab_is)

	def __str__(self):
		return self.state