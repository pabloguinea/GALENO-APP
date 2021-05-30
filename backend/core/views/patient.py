from django.shortcuts import render

import rest_framework.exceptions as exceptions
import rest_framework.parsers
import rest_framework.renderers
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters

import rest_framework_json_api.metadata
import rest_framework_json_api.parsers
import rest_framework_json_api.renderers
from rest_framework_json_api.django_filters import DjangoFilterBackend
from rest_framework_json_api.filters import (
    OrderingFilter,
    QueryParameterValidationFilter,
)
from rest_framework_json_api.pagination import JsonApiPageNumberPagination
from rest_framework_json_api.utils import format_drf_errors
from rest_framework_json_api.views import (
    ModelViewSet,
    ReadOnlyModelViewSet,
    RelationshipView,
)

from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# import model
from core.models import Patient

# import serializers
from core.serializers import PatientSerializer, PatientDRFSerializer, PatientStatsSerializer

HTTP_422_UNPROCESSABLE_ENTITY = 422

class JsonApiViewSet(ModelViewSet):
    parser_classes = [
        rest_framework_json_api.parsers.JSONParser,
        rest_framework.parsers.FormParser,
        rest_framework.parsers.MultiPartParser,
    ]
    renderer_classes = [
        rest_framework_json_api.renderers.JSONRenderer,
        rest_framework.renderers.BrowsableAPIRenderer,
    ]
    metadata_class = rest_framework_json_api.metadata.JSONAPIMetadata

    def handle_exception(self, exc):
        if isinstance(exc, exceptions.ValidationError):
            # some require that validation errors return 422 status
            # for example ember-data (isInvalid method on adapter)
            exc.status_code = HTTP_422_UNPROCESSABLE_ENTITY
        # exception handler can't be set on class so you have to
        # override the error response in this method
        response = super(JsonApiViewSet, self).handle_exception(exc)
        context = self.get_exception_handler_context()
        return format_drf_errors(response, context, exc)

class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_url_kwarg = "pk"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(doctor_id=self.request.user.id)

    def get_object(self):
        entry_pk = self.kwargs.get(self.lookup_url_kwarg, None)
        if entry_pk is not None:
            queryset = Patient.objects.filter(doctor_id=self.request.user.id)
            return get_object_or_404(queryset, id=entry_pk)

        return super(PatientViewSet, self).get_object()

class PatientStatsListView(ListAPIView):
    serializer_class = PatientStatsSerializer
    queryset = Patient.objects.all()

    def list(self, request):
        table_name = Patient.objects.model._meta.db_table
        
        queryset = Patient.objects.raw(f"SELECT 1 as id, 'classifications' AS TYPE,  classification AS INDICATOR, COUNT ( 0 ) AS COUNT  FROM {table_name} WHERE doctor_id = '{self.request.user.id}' GROUP BY classification \
            UNION ALL SELECT 2 as id, 'confirmations' AS TYPE, CAST ( is_dm_confirmed AS CHAR ) AS INDICATOR, COUNT ( 0 ) AS COUNT  FROM {table_name} WHERE doctor_id = '{self.request.user.id}' GROUP BY is_dm_confirmed \
                UNION ALL SELECT 3 as id, 'pendding' AS TYPE, 'pendding' AS INDICATOR, COUNT ( 0 ) AS COUNT FROM {table_name} WHERE doctor_id = '{self.request.user.id}' AND is_dm_confirmed IS NULL \
                    UNION ALL SELECT 4 as id, 'total' AS TYPE, 'total' AS INDICATOR, COUNT ( 0 ) AS COUNT FROM {table_name} WHERE doctor_id = '{self.request.user.id}' ")
         
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = PatientStatsSerializer(list(queryset), many=True)
        return Response(serializer.data)