from rest_framework_json_api.views import (
    ModelViewSet
)

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated   

from core import logger

# import model
from core.models import User

# import serializers
from core.serializers import UseropenApiSerializer, ChangeCustomPasswordSerializer

class UserCustomViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UseropenApiSerializer
    lookup_url_kwarg = "pk"

    def get_object(self):
        entry_pk = self.kwargs.get(self.lookup_url_kwarg, None)
        if entry_pk is not None:
            return User.objects.get(id=entry_pk)

        return super(UserCustomViewSet, self).get_object()

    def perform_create(self, serializer):
        logger.info("saving.. ")
        # the user should be activated on confirm password
        serializer.save(is_active=False)

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangeCustomPasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)
    resource_name = False
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)