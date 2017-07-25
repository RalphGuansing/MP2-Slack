from django.conf.urls import url
from newbeginnings.views import (login_view)

from . import views

urlpatterns = [
    #Home
    url(r'^home/$', views.IndexView.as_view(), name='index'),
    
    #Register
    url(r'^register/$', views.Register.as_view(), name='register'),
    
    #login
    url(r'^login/$', login_view, name='login'),
	
	
]