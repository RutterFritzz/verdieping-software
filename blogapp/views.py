from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic

from .models import Blog

class IndexView(generic.ListView):
    model = Blog
    template_name = 'blogapp/index.html'
    context_object_name = 'blogs'

class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blogapp/detail.html'