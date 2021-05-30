

from rest_framework import serializers as drf_serilazers
from rest_framework_json_api import relations, serializers
from django.db import IntegrityError, transaction
from core.models import Patient
from datetime import datetime

class PatientSerializer(serializers.ModelSerializer):
    copyright = serializers.SerializerMethodField()
    
    def get_copyright(self, resource):
        return datetime.now().year

    def get_root_meta(self, resource, many):
        return {"api_docs": "/docs/api/patients"}
    
    def create(self, validated_data):
        patient = None
        try:
            request_user = self.context['request'].user
            
            if request_user is None:
                raise  Exception('Not user in session')
            
            validated_data["doctor"] = request_user
            print(validated_data)
            
            patient = super().create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_patient")
            
        return patient
    
    
    def update(self, instance, validated_data):
        
        request_user = self.context['request'].user
            
        if request_user is None:
            raise  Exception('Not user in session')
         
        if instance.doctor.id != request_user.id:
            raise  Exception('User not authorized')
            
        return super().update(instance, validated_data)
    
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