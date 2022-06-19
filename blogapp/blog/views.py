from curses.ascii import HT
from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog
from blog.models import Category
# Create your views here.

def index(request):
    context = {
        "blogs": Blog.objects.all().filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, 'blog_pages/index.html', context)
def blogs(request):
    context = {
        "blogs": Blog.objects.all().filter(is_active=True),
        "categories":Category.objects.all()
    }
    return render(request, 'blog_pages/blogs.html', context)
def blog_details(request, slug):
    selectedBlog = Blog.objects.get(slug=slug)
    return render(request, 'blog_pages/blog_details.html', {
        "blog" : selectedBlog
    })
def blogs_by_categories(request,slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories":Category.objects.all(),
        "selected_category": slug
    }
    return render(request, 'blog_pages/blogs.html', context)