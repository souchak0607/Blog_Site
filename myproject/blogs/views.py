from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})

def blog_page(request, slug):
    blogs = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog_page.html', {'blog': blogs})

@login_required(login_url="/users/login")
def blog_new(request):
    if request.method == "POST":
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('blogs:list')
    else:
        form = forms.CreateBlog()
    return render(request, 'blogs/blog_new.html', { 'form':form })


