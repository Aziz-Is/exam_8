
from django.urls import path
from .views import ProductList

urlpatterns = [
    path('home/', ProductList.as_view(), name = 'home')
]