from django.shortcuts import render
from django.views.generic import ListView

from kuhub.models import Blog


def home(request):
    return render(request, "kuhub/home.html")


class BlogHome(ListView):
    model = Blog
    template_name = 'kuhub/index.html'
