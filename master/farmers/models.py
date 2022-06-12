from django.db import models
# from django.contrib.auth.models import AbstractUser



class LiveStockPrices(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Farmers(models.Model):
    email = models.EmailField(max_length=188, unique=True)
    password = models.CharField(max_length=188)
    initial_balance = models.FloatField(default=500000)
    cows = models.IntegerField(default=5)
    goats = models.IntegerField(default=5)
    sheeps = models.IntegerField(default=3)


    def __str__(self):
        return self.email


class LivestockOnMarket(models.Model):
    farmer = models.ForeignKey(Farmers, on_delete=models.PROTECT)
    cows = models.IntegerField(default=0)
    goats = models.IntegerField(default=0)
    sheeps = models.IntegerField(default=0)


# class PutLivestockOnMarket(models.Model):


# class SaleHistory(models.Model):
#     seller_farmer = models.ForeignKey(Farmers, on_delete=models.PROTECT)
#     cows = models.IntegerField(default=0)
#     goats = models.IntegerField(default=0)
#     sheeps = models.IntegerField(default=0)
