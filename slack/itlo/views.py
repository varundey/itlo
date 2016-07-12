from django.shortcuts import render
from django.http import HttpResponse
from .models import State
# Create your views here.
def index(request):
	state = State.objects.all()
	return HttpResponse(state)