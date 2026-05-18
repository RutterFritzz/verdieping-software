from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Blog

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogapp/index.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogapp/detail.html', {'blog': blog})