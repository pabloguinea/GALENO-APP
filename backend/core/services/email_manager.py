from templated_mail.mail import BaseEmailMessage
from django.conf import settings

class EmailManager(BaseEmailMessage):
   
   def send(self, to, *args, **kwargs):
        
        self.render()
        
        context = self.get_context_data()
        
        self.to = to
        self.cc = kwargs.pop('cc', [])
        self.bcc = kwargs.pop('bcc', [])
        self.reply_to = kwargs.pop('reply_to', [])
        self.from_email = kwargs.pop(
            'from_email', settings.DEFAULT_FROM_EMAIL
        )
        
        # decide during the context data preparation if we should be send the email
        if context["can_send"] :
            super(BaseEmailMessage, self).send(*args, **kwargs)