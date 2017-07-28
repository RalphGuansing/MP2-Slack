from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from autoslug import AutoSlugField

class Post(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    item_photo = models.FileField(blank=True,null=True)
    item_name = models.CharField(max_length=200)
    item_quantity = models.IntegerField(default=0)
    
    item_condition = models.CharField(max_length=200)
    item_condition_slug = AutoSlugField(populate_from='item_condition', blank=True)
    
    item_type = models.CharField(max_length=200)
    item_type_slug = AutoSlugField(populate_from='item_type', blank=True)
    
    item_use = models.CharField(max_length=200)
    item_use_slug = AutoSlugField(populate_from='item_use', blank=True)
    
    tags = TaggableManager()
    
    def get_absolute_url(self):
        return reverse('index')
    
    def __str__(self):
        return self.item_name +' ('+str(self.id)+') '