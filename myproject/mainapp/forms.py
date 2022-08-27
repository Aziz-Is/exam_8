from django.contrib.auth.models import User
from django import forms
from .models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = []