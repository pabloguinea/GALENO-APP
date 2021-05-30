import os
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from core.services import UserManager
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
from django.core.mail import send_mail  

from django_rest_passwordreset.models import ResetPasswordToken
from django_rest_passwordreset.signals import reset_password_token_created
from core import logger


def photo_file_name(self, filename):
    extension = filename.split('.')[-1]
    filename = 'avatar_{}.{}'.format(self.id, extension)
    return os.path.join(f'users/', filename)

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    birth_date = models.DateField(auto_now=False, null=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to=photo_file_name, blank=True, null=True)
    last_name = models.CharField(max_length=200, null=True)
    username =models.CharField(max_length=200, null=True, unique=False)
    
    
    ADMIN = 'admin'
    DOCTOR = 'doctor'
    GUEST = 'guest'
    
    ROLE_CHOICES  = [
        (ADMIN, _('Admin User')),
        (DOCTOR, _('Doctor User')),
        (GUEST, _('Staff User')),
    ]
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, blank=True, null=True, default=DOCTOR)
    
    objects = UserManager()
    
    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return "{}".format(self.email)
    
    class Meta:
        ordering = ("first_name",)