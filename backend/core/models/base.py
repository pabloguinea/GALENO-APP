from django.db import models

class BaseModel(models.Model):
    """
    Base model  
    """

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null= True)

    class Meta:
        abstract = True