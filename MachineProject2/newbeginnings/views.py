from django.shortcuts import HttpResponse, render, redirect,HttpResponseRedirect, get_object_or_404, get_list_or_404
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
        return Post.objects.all().order_by('-id')
    
    
class Register(generic.CreateView):
    form_class = UserForm
    model = User
    template_name = 'newbeginnings/user_form.html'
    
    #display blank form
    def get(self,request):
        form =self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
def ProfileView(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = list(Post.objects.filter(user_id=user_id))
    posts = list(reversed(posts))
    return render(request, 'newbeginnings/profile.html', {'user': user, 'posts': posts })

    
def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        return HttpResponseRedirect('/home/')
    return render(request, "newbeginnings/login.html",{"form":form, "title": title})

def UserPostsView(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = list(Post.objects.filter(user_id=user_id))
    return render(request, 'newbeginnings/userposts.html', {'user': user, 'posts': posts })

class CreatePostView(generic.CreateView):
    model = Post
    fields = [
    'user_id',
    'post_text',
    'item_photo',
    'item_name',
    'item_quantity',
    'item_condition',
    'item_type',
    'item_use',
    'tags',
    ]

