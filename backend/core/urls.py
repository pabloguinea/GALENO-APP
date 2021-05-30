from django.urls import path
from .views import PatientViewSet, PatientStatsListView 
#from .views import UserCustomViewSet, ChangePasswordView 

urlpatterns = [ 
    
    path("patients",PatientViewSet.as_view({"get": "list", "post": "create"}),name="patients"),
    path("patients/report",PatientStatsListView.as_view() ,name="patients_report"),
    path("patients/<uuid:pk>",PatientViewSet.as_view({"get": "retrieve", "patch": "partial_update", "delete": "destroy"}), name="patient"),
    
]