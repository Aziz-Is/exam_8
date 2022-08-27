from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here

class Product(models.Model):
    category_choices = (("clothes", 'clothes'),("shoes",'shoes'),("shirts", 'shirts'))
    name = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(max_length=20, blank=False, null=False, choices=category_choices, default='clothes')
    description = models.TextField(blank=True, max_length=1000)
    image = models.ImageField(blank=False, upload_to='images/')

    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, blank=False, null=False)
    rating = models.IntegerField(blank=False, null=False, default=1, validators=(MinValueValidator(1),MaxValueValidator(5)))
    is_moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.text