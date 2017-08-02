from django.shortcuts import HttpResponse, render, redirect,HttpResponseRedirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Post, Offer
from django.core.paginator import Paginator
from django.views.generic import View
from newbeginnings.forms import UserForm, UserLoginForm
from taggit.models import Tag
from django.template.defaultfilters import slugify

def logout_view(request):
    logout(request)
    return render(request, "newbeginnings/welcome.html")
    # Redirect to a success page.

class UserFormView(View):
    form_class = UserForm
    template_name = 'newbeginnings/registration_form.html'
    
    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})
    
    #process form data
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            
            user = form.save(commit=False)
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            #return User objects if credentials are correct
            user = authenticate(username=username,password=password)
            
            if user is not None:
                
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/home/')
                
        return render(request, self.template_name,{'form':form})
        
class IndexView(generic.ListView):
    template_name = 'newbeginnings/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    queryset = Post.objects.all().order_by('-id')
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["loggeduser"] = self.request.user.id

        return context

    
class ProfileView(generic.ListView):
    template_name = 'newbeginnings/profile.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self, **kwargs):
        return Post.objects.filter(user_id=self.kwargs['user_id']).order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context["loggeduser"] = self.request.user.id
        context["user"] = get_object_or_404(User, pk=self.kwargs['user_id'])
        return context

class WelcomeView(TemplateView):
    template_name= 'newbeginnings/welcome.html'
    
def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user= authenticate(username=username, password=password)
        login(request,user)
        return HttpResponseRedirect('/home/')
    return render(request, "newbeginnings/login.html",{"form":form, "title": title})

def UserPostsView(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = list(Post.objects.filter(user_id=user_id))
    return render(request, 'newbeginnings/userposts.html', {'user': user, 'posts': posts, 'loggeduser':request.user.id })

class TagView(generic.ListView):
    template_name = 'newbeginnings/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)
    
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug')).order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['name'] = Tag.objects.filter(slug=self.kwargs.get('slug'))[:1].get().name
        context["loggeduser"] = self.request.user.id
        return context

class CreatePostView(generic.CreateView):
    model = Post
    fields = [
    'item_photo',
    'item_name',
    'item_quantity',
    'item_condition',
    'item_type',
    'item_use',
    'tags',
    ]
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super(CreatePostView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(CreatePostView, self).get_context_data(**kwargs)
        context["loggeduser"] = self.request.user.id
        return context
    
    
class SearchTagView(generic.ListView):
    template_name = 'newbeginnings/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)
    
    def get_queryset(self):
        return Post.objects.filter(tags__slug=slugify(self.request.GET.get("q", None))).order_by('-id')

    
    def get_context_data(self, **kwargs):
        context = super(SearchTagView, self).get_context_data(**kwargs)
        context['name'] = Tag.objects.filter(slug=slugify(self.request.GET.get("q", None)))[:1].get().name
        context["loggeduser"] = self.request.user.id
        return context
    
class ConditionView(generic.ListView):
    template_name = 'newbeginnings/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)
    
    def get_queryset(self):
        return Post.objects.filter(item_condition_slug=self.kwargs.get('condition')).order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super(ConditionView, self).get_context_data(**kwargs)
        context['name'] = Post.objects.filter(item_condition_slug=self.kwargs.get('condition'))[:1].get().item_condition
        context["loggeduser"] = self.request.user.id
        return context
    
class TypeView(generic.ListView):
    template_name = 'newbeginnings/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)
    
    def get_queryset(self):
        return Post.objects.filter(item_type_slug=self.kwargs.get('type')).order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super(TypeView, self).get_context_data(**kwargs)
        context['name'] = Post.objects.filter(item_type_slug=self.kwargs.get('type'))[:1].get().item_type
        context["loggeduser"] = self.request.user.id
        return context
    
class UseView(generic.ListView):
    template_name = 'newbeginnings/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)
    
    def get_queryset(self):
        return Post.objects.filter(item_use_slug=self.kwargs.get('use')).order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super(UseView, self).get_context_data(**kwargs)
        context['name'] = Post.objects.filter(item_use_slug=self.kwargs.get('use'))[:1].get().item_use
        context["loggeduser"] = self.request.user.id
        return context

class PostView(generic.ListView):
    template_name = 'newbeginnings/post_details.html'
    context_object_name = 'posts'
    
    def get_queryset(self, **kwargs):
        return Post.objects.filter(id=self.kwargs['post_id'])
    
    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context["loggeduser"] = self.request.user.id
        context["offers"] = Offer.objects.filter(post_id=self.kwargs['post_id'])
        return context

class MakeOfferView(generic.CreateView):
    template_name = 'newbeginnings/makeoffer.html'
    model = Offer
    fields = ['isPurchase', 'purchase_offer', 'exchange_offer']
    
    def get_context_data(self, **kwargs):
        context = super(MakeOfferView, self).get_context_data(**kwargs)
        context["loggeduser"] = self.request.user.id
