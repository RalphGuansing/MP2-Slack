from django.shortcuts import HttpResponse, render, redirect,HttpResponseRedirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Post
from django.views.generic import View
from newbeginnings.forms import UserForm, UserLoginForm
from taggit.models import Tag

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
    
    def get_queryset(self):
        return Post.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["loggeduser"] = self.request.user.id

        return context
    
    
def ProfileView(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = list(Post.objects.filter(user_id=user_id))
    posts = list(reversed(posts))
    return render(request, 'newbeginnings/profile.html', {'user': user, 'posts': posts, 'loggeduser':request.user.id })

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
    return render(request, 'newbeginnings/userposts.html', {'user': user, 'posts': posts })

class TagView(generic.ListView):
    template_name = 'newbeginnings/tag.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug')).order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['name'] = Tag.objects.filter(slug=self.kwargs.get('slug'))
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

