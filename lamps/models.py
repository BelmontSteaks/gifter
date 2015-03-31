from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    country = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    ts_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    ts_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=200)

class UserInGroup(models.Model):
    user_id = models.ForeignKey(User)
    group_id = models.ForeignKey(Group)

class List(models.Model):
    list_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    list_name = models.CharField(max_length=200)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        if not self.list_id:
            # Newly created object, so set slug
            self.slug = slugify(self.list_name)

        super(List, self).save(*args, **kwargs)
              
    def __str__(self):
        return self.list_name
    
class Gift(models.Model):
    gift_id = models.AutoField(primary_key=True)
    list = models.ForeignKey(List)
    store = models.CharField(max_length=200, null=True, blank=True, default = None)
    item = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    purchased = models.BooleanField(default = False)
    purchaser = models.ForeignKey(User, null=True, blank=True, default = None)
    cost = models.CharField(max_length=200, null=True, blank=True, default = None)
    date_purchased = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.item
    
class GiftOnList(models.Model):
    list_id = models.ForeignKey(List)
    gift_id = models.ForeignKey(Gift)
    
class ListInGroup(models.Model):
    list_id = models.ForeignKey(List)
    group_id = models.ForeignKey(Group)
