from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class AdvertisementSerializer(serializers.ModelSerializer):
    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'creator', 'status', 'created_at']

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        creator = self.context["request"].user
        open_publications_count = Advertisement.objects.select_related('creator').filter(
            status='OPEN',
            creator__username=creator).count()

        if open_publications_count >= 10:
            raise ValidationError('User cannot have more than 10 open publications.')

        return data
