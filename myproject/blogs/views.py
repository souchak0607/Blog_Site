from django.shortcuts import render
from .models import Blog
# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})

def blog_page(request, slug):
    blogs = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog_page.html', {'blog': blogs})


