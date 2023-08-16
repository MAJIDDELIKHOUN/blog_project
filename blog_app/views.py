from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .models import Article, Category, Comment, Contact_Us
from django.core.paginator import Paginator
from .forms import ContactUsForm


# Create your views here.
def postdetail_view(request, slug):
    comments = Comment.objects.all()
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
        return redirect(reverse('blog_app:article_detail', args=[slug]))
    return render(request, 'blog_app/post-details.html', {'article': article, 'comments': comments})


def postlist_view(request):
    article = Article.objects.all()
    paginator = Paginator(article, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page((page_number))
    return render(request, 'blog_app/post_list.html',
                  {'article': page_obj})


def categorydetail_view(request, slug):
    category = Category.objects.get(slug=slug)
    category_detail = category.articles.all()  # inverse model
    paginator = Paginator(category_detail, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page((page_number))
    return render(request, 'blog_app/category_detail.html', {'category_detail': page_obj})


def search_view(request):
    q = request.GET.get('q')
    article = Article.objects.filter(title__icontains=q)
    paginator = Paginator(article, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page((page_number))
    return render(request, 'blog_app/post_list.html', {'article': page_obj})


def contactus_view(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # body = request.POST.get('body')
        # Contact_Us.objects.create(name=name, email=email, subject=subject, body=body)
        if form.is_valid():
            return redirect('home_app:home')
    else:
        form = ContactUsForm()
    return render(request, 'blog_app/contact.html', {'form': form})
