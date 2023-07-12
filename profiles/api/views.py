from rest_framework import views, status
from rest_framework.response import Response
from ..models import Profile
from .serializers import ProfileSerializer


class MyProfile(views.APIView):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({"detail": "Authentication not required"}, status=status.HTTP_400_BAD_REQUEST)

        profile = Profile.objects.filter(user_id=self.request.user.id).first()
        if profile:
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
