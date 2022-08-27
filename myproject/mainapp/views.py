from django.shortcuts import render
from .models import Product, Review
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"
    paginated_by = 5





