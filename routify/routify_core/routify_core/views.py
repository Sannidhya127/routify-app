from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')