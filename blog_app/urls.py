from django.urls import path
from .views import postdetail_view, categorydetail_view,search_view,PostListView,ContactUsFormView,like

app_name = 'blog_app'
urlpatterns = [
    path('post_detail/<slug:slug>', postdetail_view, name='article_detail'),
    path('post_list', PostListView.as_view(), name='article_list'),
    path('categoryt_detail/<slug:slug>', categorydetail_view, name='category_detail'),
    path('search',search_view, name='search_article'),
    path('contact_us',ContactUsFormView.as_view(), name='contact_us'),
    path('like/<slug:sluq>/<int:pk>',like, name='like'),
]
