from django.shortcuts import render

# Create your views here.

def about_us(request):
    return render(request, 'footer/about-us.html')

def services(request):
    return render(request, 'footer/services.html')

def rules(request):
    return render(request, 'footer/rules.html')

def contact_us(request):
    return render(request, 'footer/contact-us.html')