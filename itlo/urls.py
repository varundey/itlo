from django.conf.urls import url
from . import views
urlpatterns=[
	url(r'^itlo/$', views.itlo, name= 'itlo'),
	url(r'^whtk/$', views.whtk, name= 'whtk'),
]