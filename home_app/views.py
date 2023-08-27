from django.shortcuts import render
from blog_app.models import Article, Category
from django.urls import reverse
from django.views.generic.base import TemplateView


# def Home(request):
#     recent_article=Article.objects.all()[:3]
#     return render(request, 'home_app/index.html',{'recent_article':recent_article})

class HomeView(TemplateView):
    template_name = 'home_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_article"] = Article.objects.all()[:3]
        return context
