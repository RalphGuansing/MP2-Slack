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
	
    #user
	url(r'^user/(?P<user_id>[0-9]+)/$', views.ProfileView,name='profile'),
    
    #allposts
    url(r'^user/(?P<user_id>[0-9]+)/posts/$', views.UserPostsView,name='userposts'),
    
    #createposts
    url(r'^posts/add/$', views.CreatePostView.as_view(),name='post-add'),
]