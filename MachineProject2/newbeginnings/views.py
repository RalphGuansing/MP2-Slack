from django.shortcuts import HttpResponse, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User

class IndexView(generic.ListView):
    template_name = 'newbeginnings/index.html'
    context_object_name = 'users'
    def get_queryset(self):
        return User.objects.all()
    
class Register(CreateView):
    model = User
    template_name = 'newbeginnings/user_form.html'
    fields = ['first_name', 'last_name', 'username', 'password', 'degree_program_or_office', 'profile_picture']