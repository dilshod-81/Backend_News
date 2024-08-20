from dataclasses import fields
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from .models import ContactModel, CategoryModel
from .forms import ContactForm


class ContactView(CreateView):
    model = ContactModel
    fields = '__all__'
    template_name = 'pages/contact.html'
    success_url = reverse_lazy('category_page')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = CategoryModel.objects.all()
        return context
  
class CategoryView(ListView):
    model = CategoryModel
    template_name = 'home.html'

    
  