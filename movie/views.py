from rest_framework import status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from movie.models import SuspiciousUser, Rate
from movie.serializers import RatingSerializer, SuspiciousUserSerializer


class SuspiciousUsers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        suspicious_users = SuspiciousUser.objects.filter(is_return=False).all()
        for user in suspicious_users:
            user.is_return = True
            user.save()
        serializer = SuspiciousUserSerializer(suspicious_users, many=True)
        return Response(serializer.data)


class MovieRating(APIView):
    queryset = Rate.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
