from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from market.models import Market, Like
# Create your views here.
def home(request):
    user=request.user
    liked=Like.objects.select_related()
    return render(request, 'home.html', {'user':user, 'like':liked})