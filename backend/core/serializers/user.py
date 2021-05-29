

from rest_framework import serializers as drf_serilazers
from rest_framework_json_api import relations, serializers
from core.models import User
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    copyright = serializers.SerializerMethodField()
    
    def get_copyright(self, resource):
        return datetime.now().year

    def get_root_meta(self, resource, many):
        return {"api_docs": "/docs/api/users"}
    
    class Meta:
        model = User
        fields = ('id','email','first_name', 'last_name', 'birth_date', 'last_login','avatar')
        meta_fields = ("copyright",)
