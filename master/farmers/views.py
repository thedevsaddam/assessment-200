from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Farmers, LivestockOnMarket, SalePurchaseHistory
from .serializers import FarmersSerializer, LivestockOnMarketSerializer, SalePurchaseHistorySerializer
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
        print("---------------------")
        data = JSONParser().parse(request)
        print("DATAAAAA", data)
        print("--------------")

        farmer_id = Farmers.objects.get(id=data['farmer'])
        farmers_total_cow = farmer_id.cows
        farmers_total_goats = farmer_id.goats
        farmers_total_sheeps = farmer_id.sheeps

        if farmers_total_cow-data['cows'] <0 or farmers_total_goats-data['goats']<0 or farmers_total_sheeps-data['sheeps']<0:
            return HttpResponse("You don't have enough livestock")
        else:
            farmer_id.cows -= data['cows']
            farmer_id.goats -= data['goats']
            farmer_id.sheeps -= data['sheeps']
            farmer_id.save()
            serializer = LivestockOnMarketSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def sale_purchase_history(request):
    if request.method == 'GET':
        sale_purchase_data = SalePurchaseHistory.objects.all()
        serializer = SalePurchaseHistorySerializer(sale_purchase_data, many=True)
        return JsonResponse(serializer.data, safe=False) 

    if request.method == 'POST':
        data = JSONParser().parse(request)

        market_id = LivestockOnMarket.objects.get(id=data['market_id'])
        market_seller = market_id.farmer.id 
        current_seller = data['seller_farmer_id']

        if market_seller!=current_seller or current_seller==data['customer_farmer_id']:
            return HttpResponse("Please enter correct customer/seller")

        cows_in_market = market_id.cows
        goats_in_market = market_id.goats
        sheeps_in_market = market_id.sheeps

        if data['cows']>cows_in_market or data['goats']>goats_in_market or data['sheeps']>sheeps_in_market:
            return HttpResponse("Invalid livestock number")

        if data['cows'] == 0 and data['goats'] == 0 and data['sheeps'] == 0:
            return HttpResponse("No livestocks")

        market_id.cows -= data['cows']
        market_id.goats -= data['goats']
        market_id.sheeps -= data['goats']
        market_id.save()
        
        livestock_price_total = data['cows']*10000+data['goats']*8000+data['sheeps']*5000
        seller_id = Farmers.objects.get(id=market_seller)
        seller_id.initial_balance+=livestock_price_total
        seller_id.save()
        customer_id = Farmers.objects.get(id=data['customer_farmer_id'])
        customer_id.initial_balance -= livestock_price_total
        customer_id.cows += data['cows']
        customer_id.goats += data['goats']
        customer_id.sheeps += data['sheeps']
        customer_id.save()

        serializer = SalePurchaseHistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)





        






