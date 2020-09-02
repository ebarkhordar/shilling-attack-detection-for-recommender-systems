from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from movie.models import Rate, SuspiciousUser


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['user_id', 'movie_id', 'rating', 'timestamp']
        validators = [
            UniqueTogetherValidator(
                queryset=Rate.objects.all(),
                fields=['user_id', 'movie_id', 'rating', 'timestamp'],
                message="the rate is duplicate"
            )
        ]


class SuspiciousUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspiciousUser
        fields = ['user_id']
