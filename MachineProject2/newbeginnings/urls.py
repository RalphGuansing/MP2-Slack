from django.conf.urls import url
from newbeginnings.views import (login_view)

from . import views

urlpatterns = [
    #Welcome
    url(r'^$', views.WelcomeView.as_view(), name='welcome'),
    
    #Home
    url(r'^home/$', views.IndexView.as_view(), name='index'),
    
    #AcceptOffer
    url(r'^home/offer/(?P<offer_id>[0-9]+)/accepted/$', views.AcceptOffer, name='AcceptOffer'),
    
    #DeclineOffer
    url(r'^home/offer/(?P<offer_id>[0-9]+)/declined/$', views.DeclineOffer, name='DeclineOffer'),
    
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
    
    #createpurchaseoffer
    url(r'^posts/(?P<post_id>[0-9]+)/offers/add/purchase/$', views.CreatePurchaseOfferView.as_view(),name='offer-add-purchase'),
    
    #createexchangeoffer
    url(r'^posts/(?P<post_id>[0-9]+)/offers/add/exchange/$', views.CreateExchangeOfferView.as_view(),name='offer-add-exchange'),
    
    #editoffer
    #url(r'^posts/(?P<post_id>[0-9]+)/offers/add/$', views.CreateOfferView.as_view(),name='offer-add'),
    
    #editpurchaseoffer
    url(r'^posts/(?P<post_id>[0-9]+)/offers/edit/purchase/(?P<offer_id>[0-9]+)/$', views.UpdatePurchaseOfferView.as_view(),name='offer-edit-purchase'),
    
    #editexchangeoffer
    url(r'^posts/(?P<post_id>[0-9]+)/offers/edit/exchange/(?P<offer_id>[0-9]+)/$', views.UpdateExchangeOfferView.as_view(),name='offer-edit-exchange'),
    
    #deleteoffer
    url(r'^posts/(?P<post_id>[0-9]+)/offers/delete/(?P<offer_id>[0-9]+)/$', views.DeleteOfferView.as_view(),name='offer-delete'),

    #logout
    url(r"^logout/$", views.logout_view,name='logout'),
    
]