from django.shortcuts import HttpResponse, render, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.shortcuts import render
from .models import User, Post
from django.views.generic import View
from newbeginnings.forms import UserForm, UserLoginForm




class IndexView(generic.ListView):
    template_name = 'newbeginnings/index.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.all()
    
    

    
class Register(generic.CreateView):
    form_class = UserForm
    model = User
    template_name = 'newbeginnings/user_form.html'
    fields = ['first_name', 'last_name', 'username', 'password', 'degree_program_or_office', 'profile_picture']
    
    #display blank form
    def get(self,request):
        form =self.form_class(None)
        return render(request, self.template_name, {'form':form})
    

    

def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        return HttpResponseRedirect('/home/')
    return render(request, "newbeginnings/login.html",{"form":form, "title": title})
    

