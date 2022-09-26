from pyexpat import model
from tkinter import Widget
from django.db import models

# Create your models here.
# class Doctor(models.Model):

#     first_name = models.CharField(('first name'), max_length=30, blank=True)
#     last_name = models.CharField(('last name'), max_length=30, blank=True)
#     profile_picture = models.ImageField(default='default.jpg',upload_to='profile_images')
#     username = models.CharField(('username'),max_length=100,blank=True)
#     email = models.CharField(('email'), unique=True,max_length=40,blank=True)
#     address = models.CharField(max_length=200)
#     password = models.CharField(max_length=50)
#     ConfirmPassword = models.CharField(max_length=50)

#     def __str__(self):
#         return self.first_name


# class Patient(models.Model):
   
#     first_name = models.CharField(('first name'), max_length=30, blank=True)
#     last_name = models.CharField(('last name'), max_length=30, blank=True)
#     profile_picture = models.ImageField(default='default.jpg',upload_to='profile_images')
#     username = models.CharField(('username'),max_length=100,blank=True)
#     email = models.CharField(('email'), unique=True,max_length=40,blank=True)
#     address = models.CharField(max_length=200)
#     password = models.CharField(max_length=50)
#     ConfirmPassword = models.CharField(max_length=50)

#     def __str__(self):
#         return self.first_name

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _
import uuid
from .managers import UserManager
from django.shortcuts import reverse

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(('username'),max_length=100,blank=True)
    email = models.CharField(('email'), unique=True,max_length=40,blank=True)
    total_login_devices = models.IntegerField(default=0)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    profile_picture = models.ImageField(default='default.jpg',upload_to='profile_images')
    address = models.CharField(max_length=200)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)