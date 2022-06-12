from django.contrib import admin
from .models import Farmers, LiveStockPrices, LivestockOnMarket, SalePurchaseHistory


admin.site.register(Farmers)
# admin.site.register(LiveStockPrices)
admin.site.register(LivestockOnMarket)
admin.site.register(SalePurchaseHistory)