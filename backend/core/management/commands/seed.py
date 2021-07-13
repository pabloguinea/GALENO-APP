from django.core.management.base import BaseCommand, CommandError
from core.models import User
from core import logger
import os

# see here to documentation: https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/
class Command(BaseCommand):
    help = 'Seed initial data'

    def add_arguments(self, parser):
        #parser.add_argument('arg_id', nargs='+', type=int)
        pass 
    
    def seed_users(self):
        current = User.objects.count()
        
        if current > 0:
            logger.debug("User already populated...")
            return False
        
        # create super user 
        DJANGO_DB_NAME = os.environ.get('SQL_DATABASE')
        DJANGO_SU_NAME = os.environ.get('DJANGO_SUPERUSER_FIRST_NAME')
        DJANGO_SU_EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        superuser = User.objects.create_superuser(
            email=DJANGO_SU_EMAIL,
            first_name=DJANGO_SU_NAME,
            last_name=None,
            username=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)

        superuser.save()

        logger.debug("User categories inserted...")

    def handle(self, *args, **options):
        self.seed_users()
        logger.debug("End Seed...")