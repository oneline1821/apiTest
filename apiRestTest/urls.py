from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from rest_framework.authtoken import views


urlpatterns = [
	url(r'api/v1/', include('rest.urls' , namespace='person')),
    url('admin/', admin.site.urls),
]

urlpatterns += [
	url(r'api/v1/auth', include(rest_framework.urls , namespace='rest_framework'))
]
