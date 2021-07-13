from django.urls import path, include
from django.conf.urls import url, patterns
from .views import PatientViewSet, PatientStatsListView 
#from .views import UserCustomViewSet, ChangePasswordView 

base_urlpatterns = [ 
    
    path("patients",PatientViewSet.as_view({"get": "list", "post": "create"}),name="patients"),
    path("patients/report",PatientStatsListView.as_view() ,name="patients_report"),
    path("patients/<uuid:pk>",PatientViewSet.as_view({"get": "retrieve", "patch": "partial_update", "delete": "destroy"}), name="patient"),
    
]


urlpatterns = [
    url(r'^', include(base_urlpatterns)),
    url(r'^api/backend/', include(base_urlpatterns)),
]