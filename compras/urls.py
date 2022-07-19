from django.urls import path
from .views import novo_cliente

urlpatterns = [
    path('checkout', novo_cliente, name='novo_cliente'),
]