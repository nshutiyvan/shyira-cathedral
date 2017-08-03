from django.db import models
from django.utils.text import slugify
from  django.forms import ModelForm
from django.utils.crypto import get_random_string
from django.core.urlresolvers import reverse
# Create your models here.
def image_upload_to(instance, filename):
    image=instance.image
    slug = get_random_string(length=20)
    return "gallery/%s" % (slug)
class Album(models.Model):
    name=models.CharField(max_length=120)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.name

class Image(models.Model):
    album=models.ForeignKey(Album)
    image=models.ImageField(upload_to=image_upload_to)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    def __str__(self):
        return str(self.image)
class Event(models.Model):
    due=models.DateTimeField()
    title=models.CharField(max_length=120)
    details=models.TextField(null=True,blank=True)
    address=models.CharField(max_length=120)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    def __str__(self):
        return  self.title
class Message(models.Model):
    firstname=models.CharField(max_length=120,blank=True,default='none')
    lastname=models.CharField(max_length=120,blank=True,default='none')
    email=models.CharField(max_length=120,null=True)
    message=models.TextField()

    def __str__(self):
        return self.email
class MessageForm(ModelForm):
    class Meta:
        model=Message
        fields=['firstname','lastname','email','message']

SITE_ID=1        