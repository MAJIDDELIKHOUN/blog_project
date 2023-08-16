from django.urls import path
from .views import postdetail_view, postlist_view, categorydetail_view,search_view,contactus_view

app_name = 'blog_app'
urlpatterns = [
    path('post_detail/<slug:slug>', postdetail_view, name='article_detail'),
    path('post_list', postlist_view, name='article_list'),
    path('categoryt_detail/<slug:slug>', categorydetail_view, name='category_detail'),
    path('search',search_view, name='search_article'),
    path('contact_us',contactus_view, name='contact_us'),
]
