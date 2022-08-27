from django.shortcuts import render, redirect
from .models import Product, Review
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .forms import ProductForm


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