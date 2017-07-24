from django.shortcuts import HttpResponse, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.shortcuts import render
from .models import User, Post
from newbeginnings.forms import UserForm


class IndexView(generic.ListView):
    template_name = 'newbeginnings/index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.all()
    
class Register(generic.CreateView):
    model = User
    template_name = 'newbeginnings/user_form.html'
    fields = ['first_name', 'last_name', 'username', 'password', 'degree_program_or_office', 'profile_picture']
    
    def get(self,request):
        form =UserForm()
        return render(request, self.template_name, {'form':form})