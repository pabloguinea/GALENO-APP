from django.contrib.auth.tokens import default_token_generator
#from templated_mail.mail import BaseEmailMessage
from core.services import EmailManager

from djoser import utils
from djoser.conf import settings


class ActivationEmail(EmailManager):
    template_name = "email/activation.html"

    def get_context_data(self):
        
        context = super().get_context_data()

        user = context.get("user")
        print(f"User is Active: {user.is_active}")
        # Mark a condition to allow send the activation email
        context["can_send"] =  not user.is_active
        
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)
        return context
