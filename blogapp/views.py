from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views import generic

from blogapp.forms import BlogForm

from .models import Blog

class IndexView(generic.ListView):
    model = Blog
    template_name = 'blogapp/index.html'
    context_object_name = 'blogs'

class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blogapp/detail.html'

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blogapp:index')
    else:
        form = BlogForm()
    return render(request, 'blogapp/create.html', {'form': form})