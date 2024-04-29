from django.urls import path
from . import views

urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
    path('rules-and-terms/', views.rules, name='rules'),
    path('contact_us/', views.contact_us, name='contact_us'),
]