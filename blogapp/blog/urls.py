from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("categories/<slug:slug>",views.blogs_by_categories, name="blogs_by_categories"),
    path("blogs/<slug:slug>", views.blog_details, name="blog_details")
]
