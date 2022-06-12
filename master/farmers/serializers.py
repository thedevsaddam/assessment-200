from dataclasses import field
from rest_framework import serializers
from .models import Farmers, LivestockOnMarket, SalePurchaseHistory


class FarmersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmers
        fields = '__all__'


class LivestockOnMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockOnMarket
        fields = '__all__'

class SalePurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SalePurchaseHistory
        fields = '__all__'

      