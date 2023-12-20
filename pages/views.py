from django.shortcuts import render, redirect
from pages.models import MainScrollMode

def home_view(request):
    scrolls = MainScrollMode.objects.all().order_by('-pk')
    context = {
        'scrolls':scrolls
    }
    return render(request, "index.html", context)

def Menu_next_view(request):
    food = MainScrollMode.objects.all().order_by('-pk')
    context = {
        'foods':food
    }
    return render(request, "index.html", context)