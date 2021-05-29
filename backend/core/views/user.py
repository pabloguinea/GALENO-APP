from rest_framework_json_api.views import (
    ModelViewSet
)

# import model
from core.models import User

# import serializers
from core.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "pk"

    def get_object(self):
        entry_pk = self.kwargs.get(self.lookup_url_kwarg, None)
        if entry_pk is not None:
            return User.objects.get(id=entry_pk)

        return super(UserViewSet, self).get_object()
