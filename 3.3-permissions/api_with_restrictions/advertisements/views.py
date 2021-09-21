from django_filters import rest_framework as filters

from .permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter
