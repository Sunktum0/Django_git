from django.urls import path
from .views import ClassBasedView, FunctionalView

urlpatterns = [
    path('class-view/', ClassBasedView.as_view(), name='class_view'),
    path('functional-view/', FunctionalView, name='functional_view'),
]