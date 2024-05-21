from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blog_list, name="list" ),
    path('<slug:slug>', views.blog_page, name="page" ),
]