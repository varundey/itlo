from django.conf.urls import url
from . import views
urlpatterns=[
	url(r'^$', views.itlo, name= 'itlo'),
	url(r'^whtk/$', views.whtk, name= 'whtk'),
]