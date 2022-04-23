from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'projectunit/home.html', context)


def about(request):
    return render(request, 'projectunit/about.html', {'title': 'About'})
