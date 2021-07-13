from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    #def create_user(self, email, first_name, area=None, card_id = None, last_name=None, password=None):
    def create_user(self, **validated_data):
        
        email = validated_data["email"]
        first_name = validated_data["first_name"]
        area = validated_data["area"]
        card_id = validated_data["card_id"]
        password = validated_data["password"]
        is_agreements = validated_data["is_agreements"]
        
        last_name = None
        if "last_name" in validated_data:
            last_name = validated_data["last_name"]
            
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        
        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.is_agreements = is_agreements
        user.area = area
        user.card_id = card_id
        user.set_password(password)  # change password to hash
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name=None, username=None, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        
        if not username:
            username = email
            
        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)  # change password to hash
        user.is_admin = True
        user.is_staff = True
        user.role = "admin"
        user.area = None
        user.is_active=True
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, first_name, last_name=None,  username=None, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        
        if not username:
            username = email
        
        if not last_name:
            last_name = ""
            
        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)  # change password to hash
        user.is_admin = True
        user.is_staff = True
        user.role = "admin"
        user.area = None
        user.is_active=True
        user.save(using=self._db)
        return user