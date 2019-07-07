from rest_framework import serializers
from .models import AllClothes

class AllClothesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AllClothes
        fields = ('item_Name', 'item_location')