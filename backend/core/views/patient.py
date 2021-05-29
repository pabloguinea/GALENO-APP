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

# import model
from core.models import Patient

# import serializers
from core.serializers import PatientSerializer, PatientDRFSerializer

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

    def get_object(self):
        entry_pk = self.kwargs.get(self.lookup_url_kwarg, None)
        if entry_pk is not None:
            return Patient.objects.get(id=entry_pk)

        return super(PatientViewSet, self).get_object()

class PatientCustomViewSet(JsonApiViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DRFPatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientDRFSerializer
    #lookup_url_kwarg = "entry_pk"

    def get_object(self):
    #    entry_pk = self.kwargs.get(self.lookup_url_kwarg, None)
    #    if entry_pk is not None:
    #        return Entry.objects.get(id=entry_pk).blog

        return super(DRFPatientViewSet, self).get_object()

class PatientListAPIView(ListAPIView):
    """Lists all from the database"""
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientCreateAPIView(CreateAPIView):
    """Creates a new """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientUpdateAPIView(UpdateAPIView):
    """Update  whose id has been passed through the request"""
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDeleteAPIView(DestroyAPIView):
    """Deletes  whose id has been passed through the request"""
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer