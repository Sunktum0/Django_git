from django.urls import path
from . import views  # Импортируем представления

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('shop/', views.shop, name='shop'),  # Страница магазина
    path('cart/', views.cart, name='cart'),  # Страница корзины
    path('example/', views.example_view, name='example_view'),  # Пример страницы
]