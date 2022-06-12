from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Farmers, LivestockOnMarket
from .serializers import FarmersSerializer, LivestockOnMarketSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def farmers_data(request):
    if request.method == 'GET':
        farmer = Farmers.objects.all()
        serializer = FarmersSerializer(farmer, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FarmersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def livestock_on_market(request):
    if request.method == 'GET':
        market_livestocks = LivestockOnMarket.objects.all()
        serializer = LivestockOnMarketSerializer(market_livestocks, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = data = JSONParser().parse(request) 

        farmer_id = Farmers.objects.get(id=data['farmer'])
        farmers_total_cow = farmer_id.cows
        farmers_total_goats = farmer_id.goats
        farmers_total_sheeps = farmer_id.sheeps

        if farmers_total_cow-data['cows'] <0 or farmers_total_goats-data['goats']<0 or farmers_total_sheeps-data['sheeps']<0:
            return HttpResponse("You don't have enough livestock")
        else:
            serializer = LivestockOnMarketSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)




