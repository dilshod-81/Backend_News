from django.urls import path

from .views import ContactView, CategoryView

urlpatterns = [
    path('', CategoryView.as_view(), name='category_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    #path('contact/', category, name='contact_page'),

]