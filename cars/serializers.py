from decimal import Decimal
from cars.models import Car, Owner
from rest_framework import serializers




class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id','name','adress','city']


class CarSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
            model = Car
            fields = ['id', 'car_make', 'car_model','year','registration','fuel','owner']
