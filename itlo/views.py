from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import State, Keys
import json
# Create your views here.

def itlo(request):
	state = str(State.objects.all()[0])

	if state=="Open!":
		data = {"text": "*Awesome!*\nThe lab is open right now. :+1:"}
		json_data = json.dumps(data)
		return HttpResponse(json_data, content_type='application/json')
	else:
		data = {"text": "*Oopsies!*\nThe lab is closed right now. :confused:"}
		json_data = json.dumps(data)		
		return HttpResponse(json_data, content_type='application/json')

def whtk(request):
	keys = list(Keys.objects.values())

	for i in keys:
		i.pop('id')
		i['author_name']=i.pop('keys')

	data = {"text":'The following guys have the key:\n', 'attachments':keys}
	json_data = json.dumps(data)

	return HttpResponse(json_data, content_type='application/json')