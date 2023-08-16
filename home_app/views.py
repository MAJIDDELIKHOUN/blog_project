from django.shortcuts import render
from blog_app.models import Article,Category
from django.urls import reverse

def Home(request):
    article=Article.objects.all()
    recent_article=Article.objects.all()[:3]
    categories=Category.objects.all()
    return render(request, 'home_app/index.html',{'article':article,'recent_article':recent_article,'categories':categories})
