from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

from blogapp.forms import BlogForm

from .models import Blog

class IndexView(generic.ListView):
    model = Blog
    template_name = 'blogapp/index.html'
    context_object_name = 'blogs'

class DetailView(generic.DetailView):
    model = Blog
    queryset = Blog.objects.select_related('author')
    template_name = 'blogapp/detail.html'

class ProfileView(generic.DetailView):
    model = User
    template_name = 'blogapp/profile.html'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('blogapp:index')
    else:
        form = AuthenticationForm()
    return render(request, 'blogapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('blogapp:index')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogapp:login')
    else:
        form = UserCreationForm()
    return render(request, 'blogapp/register.html', {'form': form})

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

def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogapp:index')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogapp/edit.html', {'form': form, 'blog': blog})

def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('blogapp:index')
