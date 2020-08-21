from rest_framework import serializers

from movie.models import Rate, SuspiciousUser


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['user_id', 'movie_id', 'rating', 'timestamp']


class SuspiciousUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspiciousUser
        fields = ['user_id']
