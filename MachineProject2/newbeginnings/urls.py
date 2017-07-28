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
    
    #login
    url(r'^login/$', login_view, name='login'),
	
    #user
	url(r'^user/(?P<user_id>[0-9]+)/$', views.ProfileView.as_view(),name='profile'),
    
    #allposts
    url(r'^user/(?P<user_id>[0-9]+)/posts/$', views.UserPostsView,name='userposts'),
    
    #createposts
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.PostView.as_view(),name='post'),
    
    #createposts
    url(r'^posts/add/$', views.CreatePostView.as_view(),name='post-add'),
    
    #tags
    url(r'^posts/tag/(?P<slug>[-\w]+)/$', views.TagView.as_view(),name='post-tag'),
    
    #condition
    url(r'^posts/condition/(?P<condition>[-\w]+)/$', views.ConditionView.as_view(),name='post-condition'),
    
    #type
    url(r'^posts/type/(?P<type>[-\w]+)/$', views.TypeView.as_view(),name='post-type'),
    
    #use
    url(r'^posts/use/(?P<use>[-\w]+)/$', views.UseView.as_view(),name='post-use'),
    
    #searchtag
    url(r'^posts/search/tag/$', views.SearchTagView.as_view(),name='searchTag'),
    
    #searchcondition
   # url(r'^posts/search/tag/$', views.SearchTagView.as_view(),name='searchTag'),

    #logout
    url(r"^logout/$", views.logout_view,name='logout'),
    
]