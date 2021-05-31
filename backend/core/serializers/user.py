

from rest_framework import serializers as drf_serilazers, exceptions
from rest_framework_json_api import relations, serializers
from core.models import User
from datetime import datetime
from django.test.utils import override_settings

from djoser import utils
from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings
from django.conf import settings as all_seetings

class UserCustomSerializer(drf_serilazers.ModelSerializer):
    
    class Meta:
        model = User
        #fields = tuple(User.REQUIRED_FIELDS) + (
        #    settings.USER_ID_FIELD,
        #    settings.LOGIN_FIELD,
        #)
        fields = ('id','email','first_name', 'last_name', 'birth_date', 'last_login','avatar', 'role', 'card_id', 'area', 'is_agreements')
        read_only_fields = (settings.LOGIN_FIELD,)

    
    def update(self, instance, validated_data):
        
        print("Updating user: ")
        print(validated_data)
        
        email_field = get_user_email_field_name(User)
        
        """ This not make sense """
        if settings.SEND_ACTIVATION_EMAIL and email_field in validated_data :
            instance_email = get_user_email(instance)
            if instance_email != validated_data[email_field]:
                instance.is_active = False
                instance.save(update_fields=["is_active"])
        
        
        return super().update(instance, validated_data)
        
    
class UseropenApiSerializer(serializers.ModelSerializer):
    copyright = serializers.SerializerMethodField()
    
    def get_copyright(self, resource):
        return datetime.now().year

    def get_root_meta(self, resource, many):
        return {"api_docs": "/docs/api/users"}
    
    
    class Meta:
        model = User
        fields = ('id','email','first_name', 'last_name', 'birth_date', 'last_login','avatar', 'role', 'card_id', 'area', 'is_agreements')
        #fields = '__all__'
        meta_fields = ("copyright",)

class ChangeCustomPasswordSerializer(drf_serilazers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = drf_serilazers.CharField(required=True)
    new_password = drf_serilazers.CharField(required=True)