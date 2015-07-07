from django.shortcuts import render
from articles.models import Articles

def home(request):
    article = Articles.objects.order_by('-date')[0]
    return render(request, 'home.html', {'article':article})

def allpost(request):
    articles = Articles.objects.order_by('-date')
    return render(request, 'allpost.html', {'articles':articles})
