from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')