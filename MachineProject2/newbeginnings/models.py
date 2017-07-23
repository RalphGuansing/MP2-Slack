from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    degree_program_or_office = models.CharField(max_length=200)
    profile_picture = models.FileField()
    
    def get_absolute_url(self):
        return reverse('index')
    
    def __str__(self):
        return self.username
    
class Post(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    post_text = models.CharField(max_length=200)