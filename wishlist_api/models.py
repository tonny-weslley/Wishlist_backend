from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(
        upload_to='users/cover', null=True, blank=True)
    joined_in = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

class List(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' de ' + self.user.name


class Wish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to='wishes/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' em ' + self.list.name

