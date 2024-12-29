from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Food
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q


def home(request):
    item_list = Food.objects.all()
    context={
        'foods':item_list
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')