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

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, required=True,
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput, strip=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password_confirm != password:
            raise forms.ValidationError('Пароли не совпадают')

        first_name = cleaned_data.get("first_name")
        print(first_name)
        if first_name == '':
            raise forms.ValidationError('Заполните имя')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    class Meta:
        model = User
        exclude = []
