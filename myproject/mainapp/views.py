from django.shortcuts import render, redirect
from .models import Product, Review
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .forms import ProductForm, ReviewForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm



# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"
    paginated_by = 5

class ProductView(TemplateView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=context['pk'])
        context['reviews'] = Review.objects.filter(product_id=context['pk'])
        print(context)
        return context

class AddProductView(TemplateView):
    template_name = "add.html"
    form = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_form'] = self.form()
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
        return render(request, 'add.html', {'my_form': form})


class UpdateView(TemplateView):
    template_name = "add.html"
    form = ProductForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Product.objects.get(pk=context['pk'])
        context['my_form'] = self.form(
            initial={'name': obj.name, 'category': obj.category, 'description': obj.description,
                     'image': obj.image})
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST,  request.FILES)
        if form.is_valid():
            obj = Product.objects.get(pk=kwargs['pk'])
            obj.name = form.cleaned_data['name']
            obj.category = form.cleaned_data['category']
            obj.description = form.cleaned_data['description']
            obj.image = form.cleaned_data['image']
            obj.save()
            return redirect('home')
        return render(request, 'add.html', {'my_form': form})


class DeleteView(TemplateView):
    template_name = 'delete.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Product.objects.get(pk=context['pk'])
        context['product'] = obj
        return context
    def post(self, request, *args, **kwargs):
        obj = Product.objects.get(pk=kwargs['pk'])
        if obj:
            obj.delete()
            return redirect('home')
        return render (request,'delete.html', {'task':obj})


# path(xxx/<int:pk>/)
class ReviewsListView(ListView):
    model = Review
    template_name = "detail.html"
    context_object_name = "reviews"


class AddReview(TemplateView):
    template_name = 'add_review.html'
    form = ReviewForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_form'] = self.form()
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
        return render(request, 'add_review.html', {'my_form': form})


class UpdateReview(TemplateView):
    template_name = "add_review.html"
    form = ReviewForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Review.objects.get(pk=context['pk'])
        context['my_form'] = self.form(
            initial={'author': obj.author, 'product': obj.product, 'text': obj.text,
                     'rating': obj.rating})
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST,  request.FILES)
        if form.is_valid():
            obj = Review.objects.get(pk=kwargs['pk'])
            obj.author = form.cleaned_data['author']
            obj.product = form.cleaned_data['product']
            obj.text = form.cleaned_data['text']
            obj.rating = form.cleaned_data['rating']
            obj.save()
            return redirect('home')
        return render(request, 'add_review.html', {'my_form': form})


class DeleteReview(TemplateView):
    template_name = 'delete_review.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Review.objects.get(pk=context['pk'])
        context['review'] = obj
        return context
    def post(self, request, *args, **kwargs):
        obj = Review.objects.get(pk=kwargs['pk'])
        if obj:
            obj.delete()
            return redirect('home')
        return render(request, 'delete_review.html', {'task': obj})

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context['has error'] = True
    return render (request, 'login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('home')

def register_user(request, *args, **kwargs):
    if request.method == 'POST':
        my_form = RegisterForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect('login')
    else:
        my_form = RegisterForm()
    return render(request, 'register.html', {'form': my_form})
