
from rest_framework.response import Response
from rest_framework.views import APIView

# import model
from core.models import User

# import serializers
from core.serializers import UserSerializer

class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "pk"

    def post(self, request, format=None):
        try:
            # exist then update
            profile = User.objects.get(id=request.user.id)
            serializer = UserSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)