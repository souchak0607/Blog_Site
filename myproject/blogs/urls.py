from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blog_list, name="list" ),
    path('new-post/', views.blog_new, name="new-post" ),
    path('<slug:slug>', views.blog_page, name="page" ),
]