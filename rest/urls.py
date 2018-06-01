from django.conf.urls import url
from rest.views import *

urlpatterns = [
	url(r'^person/$', PersonList.as_view(), name = 'person')
]