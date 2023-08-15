from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings
#from drf_yasg.views import get_schema_view
#from drf_yasg import openapi


from rest_framework.schemas import get_schema_view
from rest_framework_json_api.schemas.openapi import SchemaGenerator

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


# Swagger documentation setup
#schema_view = get_schema_view(
#    openapi.Info(
#        title="IRS API",
#        default_version='v1',
#        description="Api description",
#        terms_of_service="https://www.google.com/policies/terms/",
#        contact=openapi.Contact(email="contact@snippets.local"),
#        license=openapi.License(name="MIT License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
#)

schema_view = get_schema_view(
            title="Galeno APP API",
            description="Galeno APP API allow to manage all the information in the system.",
            version="1.0.0",
            generator_class=SchemaGenerator,
        )

base_urlpatterns = [
    # admin urls
    path('admin/', admin.site.urls),
    
    # user urls 
    path('v1/auth/', include('rest_framework.urls')),
    
    # modules urls + open api 3.0 standard support
    # https://readthedocs.org/projects/django-rest-framework-json-api/downloads/pdf/stable/
    path('v1/', include("core.urls")),
    
    # reset password flow
    #url(r'^v1/account/password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
    #oauth 2.0 server
    re_path(r'^v1/oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    #jwt 
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage
    re_path(r'^v1/auth/', include('djoser.urls')),
    re_path(r'^v1/auth/', include('djoser.urls.jwt')),
    #url(r'^v1/auth/', include('djoser.urls.authtoken')),

    #openapi 3.0 + documentation
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
]

# add url media and static content
base_urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    re_path(r'^', include(base_urlpatterns)),
    re_path(r'^api/backend/', include(base_urlpatterns)),
]

urlpatterns = [
    url(r'^', include(base_urlpatterns)),
    url(r'^api/backend/', include(base_urlpatterns)),
]
