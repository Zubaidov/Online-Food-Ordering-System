from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contact_mail(request):
    user_fname = request.GET['name']
    user_fname = request.GET['email']