from django.urls import path
from . import views

urlpatterns = [
    path('', views.farmers_data, name='farmers_data'),
    path('market/', views.livestock_on_market, name = 'livestock_on_market'),
    path('sale_purchase_history/', views.sale_purchase_history, name = 'sale_purchase_history'),

]
