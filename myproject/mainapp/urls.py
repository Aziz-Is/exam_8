
from django.urls import path
from .views import ProductList, ProductView, AddProductView, UpdateView, DeleteView

urlpatterns = [
    path('home/', ProductList.as_view(), name='home'),
    path('product/<int:pk>/', ProductView.as_view(), name='detail'),
    path('product/add/', AddProductView.as_view(), name='add'),
    path('product/update/<int:pk>/', UpdateView.as_view(), name='update'),
    path('product/delete/<int:pk>/', DeleteView.as_view(), name='delete'),
]