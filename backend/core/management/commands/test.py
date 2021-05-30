from django.core.management.base import BaseCommand, CommandError
from core.models import User
from core import logger
import os  
from django.core.mail import send_mail
from django.core.mail import EmailMessage


# see here to documentation: https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/
class Command(BaseCommand):
    help = 'Seed initial data'

    def add_arguments(self, parser):
        #parser.add_argument('arg_id', nargs='+', type=int)
        pass 
    
    
    def handle(self, *args, **options):
        send_mail(
            'prueba de correo', 
            'cuerpo del correo', 
            'info@teamcloud.com.co', 
            [
                'ramejiafernandez@gmail.com',
            ], fail_silently=False
        ) 
        
        #msg = EmailMessage(
        #    from_email='info@teamcloud.com.co',
        #    to=['ramejiafernandez@gmail.com'],
        #)
        #msg.template_id = "d-94f74e1a1dc04af99e20d1599138000c"
        #msg.dynamic_template_data = {
        #"title": "Title"
        #}
        #msg.send(fail_silently=False)
        logger.debug("End Seed...")