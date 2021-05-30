# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.utils.timezone import now
from core.models import User
from django.utils.translation import gettext as _
from . import BaseModel

class Patient (BaseModel):
    
    NON_DEMENTED = 'NonDemented'
    MILD_DEMENTED = 'MildDemented'
    MODERATED_DEMENTED = 'ModerateDemented'
    VERY_DEMENTED = 'VeryMildDemented'
    

    CLASSIFICATIONS_TYPE  = [
        (NON_DEMENTED, _('NonDemented')),
        (MILD_DEMENTED, _('MildDemented')),
        (MODERATED_DEMENTED, _('ModerateDemented')),
        (VERY_DEMENTED, _('VeryMildDemented')),
    ]
    

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200,null=False)
    email = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=200,null=True)
    birth_date = models.DateField(auto_now=False, null=True)
    classification = models.CharField(max_length=20, choices=CLASSIFICATIONS_TYPE, null=False)
    data = models.JSONField(null=True)
    is_dm_confirmed = models.BooleanField(null=True)
    
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.first_name + self.last_name
    
    class Meta:
        ordering = ("first_name",)