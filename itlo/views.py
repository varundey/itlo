from django.shortcuts import render
from django.http import HttpResponse
from .models import State
# Create your views here.
def index(request):
	state = str(State.objects.all()[0])

	if state=="Open!":
		return HttpResponse(":thumbsup: The lab is *Open!*")

	else:
		return HttpResponse(":confused: Sorry, the lab is closed right now!")
