from django.urls import path
from .views import PatientViewSet 
from .views import UserViewSet 

urlpatterns = [ 
    
    path("patient",PatientViewSet.as_view({"get": "list", "post": "create"}),name="patients"),
    path("patient/<uuid:pk>",PatientViewSet.as_view({"get": "retrieve", "patch": "partial_update", "delete": "destroy"}), name="patient"),
    
    path("user",UserViewSet.as_view({"get": "list", "post": "create"}),name="users"),
    path("user/<int:pk>",UserViewSet.as_view({"get": "retrieve", "patch": "partial_update", "delete": "destroy"}), name="user"),
    
]