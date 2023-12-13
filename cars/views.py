from cars.pagination import DefaultPagination
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from .filters import CarFilter
from .models import Car, Owner
from .serializers import CarSerializer, OwnerSerializer
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin


class CarViewSet(ModelViewSet):
    #queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CarFilter
    pagination_class = DefaultPagination
    search_fields = ['year']
    ordering_fields = ['car_make']

    def get_queryset(self):
        return Car.objects.filter(owner_id=self.kwargs['owner_pk'])

    def get_serializer_context(self):
        return {'request': self.request,'owner_id': self.kwargs['owner_pk']}

    def delete(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        if car.owner is not None:
            return Response({'error': 'car cannot be deleted because it is associated with an owner.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OwnerViewSet(ListModelMixin, CreateModelMixin,
                  RetrieveModelMixin, UpdateModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    