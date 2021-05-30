

from rest_framework import serializers as drf_serilazers
from rest_framework_json_api import relations, serializers
from core.models import Patient
from datetime import datetime

class PatientSerializer(serializers.ModelSerializer):
    copyright = serializers.SerializerMethodField()
    
    def get_copyright(self, resource):
        return datetime.now().year

    def get_root_meta(self, resource, many):
        return {"api_docs": "/docs/api/patients"}
    
    class Meta:
        model = Patient
        fields = "__all__"
        meta_fields = ("copyright",)

class PatientDRFSerializer(drf_serilazers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = "__all__"
        
class PatientStatsSerializer(drf_serilazers.Serializer):
    #model = Patient
    indicator = drf_serilazers.CharField(max_length=20, required=True)
    count = drf_serilazers.IntegerField(required=True)

    class Meta:
        fields = ('indicator', 'count')