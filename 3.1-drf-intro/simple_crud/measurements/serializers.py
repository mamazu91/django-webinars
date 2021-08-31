from rest_framework import serializers
from .models import Measurement, Project


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'latitude', 'longitude', 'image')


class MeasurementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('id', 'value', 'project')
