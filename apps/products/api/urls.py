from django.urls import path
from apps.products.api.api import product_api_view, product_detail_api_view, bill_api_view, bill_detail_api_view

urlpatterns = [
    path('productos/', product_api_view, name='productos'),
    path('productos/<int:pk>/', product_detail_api_view, name='producto_detail_api_view'),
    path('compras/', bill_api_view, name='compras'),
    path('compras/<int:pk>/', bill_detail_api_view, name='compra_detail_api_view'),
]