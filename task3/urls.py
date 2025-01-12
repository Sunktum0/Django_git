from django.urls import path
from .views import home, store, cart

urlpatterns = [
    path('', home, name='home'),
    path('store/', store, name='store'),
    path('cart/', cart, name='cart'),
]