from django.conf.urls import url
from newbeginnings.views import (login_view)

from . import views

urlpatterns = [
    #Welcome
    url(r'^$', views.WelcomeView.as_view(), name='welcome'),
    
    #Home
    url(r'^home/$', views.IndexView.as_view(), name='index'),
    
    #UserRegister
    url(r'^register/$', views.UserFormView.as_view(), name='userregister'),
    
    #Register
   # url(r'^register/$', views.Register.as_view(), name='register'),
    
    #login
    url(r'^login/$', login_view, name='login'),
	
    #user
	url(r'^user/(?P<user_id>[0-9]+)/$', views.ProfileView,name='profile'),
    
    #allposts
    url(r'^user/(?P<user_id>[0-9]+)/posts/$', views.UserPostsView,name='userposts'),
    
    #createposts
    url(r'^posts/add/$', views.CreatePostView.as_view(),name='post-add'),
    
    #tags
    url(r'^posts/tag/(?P<slug>[-\w]+)/$', views.TagView.as_view(),name='post-tag'),
    
    #logout
    url(r"^logout/$", views.logout_view,name='logout'),
    
]