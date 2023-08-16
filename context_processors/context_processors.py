from blog_app.models import Article, Category


def article(request):
    article = Article.objects.all()
    recent_article = Article.objects.all()[:3]
    categories = Category.objects.all()
    return {'article':article,'recent_article':recent_article,'categories':categories}