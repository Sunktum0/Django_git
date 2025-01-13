from django.urls import path
from .views import sign_up_by_django

urlpatterns = [
    path('', sign_up_by_django, name='sign_up_by_django'),  # Путь по умолчанию
    path('django_sign_up/', sign_up_by_django, name='sign_up_by_html'),
]