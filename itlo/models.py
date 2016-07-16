from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
@python_2_unicode_compatible
class State(models.Model):
	lab_is=(("Open!","Open"),("Close",'Close'))
	state = models.CharField(max_length=5, choices=lab_is)

	def save(self, *args, **kwargs):
		if State.objects.count() > 1:
			raise ValidationError("Can only create 1 instance") 

		super(State, self).save(*args, **kwargs)

	def __str__(self):
		return self.state

	

@python_2_unicode_compatible
class Keys(models.Model):
	keys=models.CharField(max_length=10)

	# def save(self, *args, **kwargs):
	# 	if State.objects.count() > 2:
	# 		raise ValidationError("Can create at the most 3 instances") 

	# 	super(State, self).save(*args, **kwargs)

	def __str__(self):
		return self.keys