import os
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from core.services import UserManager
from core import logger

def photo_file_name(self, filename):
    extension = filename.split('.')[-1]
    filename = 'avatar_{}.{}'.format(self.id, extension)
    print("MEDIAROOT IN MODEL ", settings.MEDIA_ROOT )
    logger.debug("Path: %s", os.path.join(settings.MEDIA_ROOT,'/users/', filename))
    return os.path.join(f'users/', filename)

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    birth_date = models.DateField(auto_now=False, null=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to=photo_file_name, blank=True, null=True)
    #is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    #is_admin = models.BooleanField(default=False)
    
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
    
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    
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