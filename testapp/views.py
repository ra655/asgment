from django.shortcuts import render,redirect
from .models import *
from .forms import *

def UserProfile(request):
    return render(request,'userprofile.html')
