from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .models import Article, Category, Comment, Contact_Us, Like
from django.core.paginator import Paginator
from .forms import ContactUsForm
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


# Create your views here.


def postdetail_view(request, slug):
    comments = Comment.objects.all()
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
        return reverse('blog_app:article_detail', args=[slug])

    return render(request, 'blog_app/post-details.html', {'article': article, 'comments': comments, })


# def postlist_view(request):
#     article = Article.objects.all()
#     paginator = Paginator(article, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page((page_number))
#     return render(request, 'blog_app/post_list.html',
#                   {'article': page_obj})


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


# def contactus_view(request):
#     if request.method == 'POST':
#         form = ContactUsForm(data=request.POST)
#         if form.is_valid():
#             # email = form.cleaned_data.get('email')
#             # name = form.cleaned_data.get('name')
#             # subject = form.cleaned_data.get('subject')
#             # body = form.cleaned_data.get('body')
#             # Contact_Us.objects.create(name=name, email=email, subject=subject, body=body)
#             form.save()
#             return redirect('home_app:home')
#     else:
#         form = ContactUsForm()
#     return render(request, 'blog_app/contact.html', {'form': form})


class PostListView(ListView):
    context_object_name = 'article'
    queryset = Article.objects.all()
    model = Article
    paginate_by = 2
    template_name = 'blog_app/post_list.html'


# class PostDetailView(DetailView):
#     model = Article
#     template_name = 'blog_app/post-details.html'


class ContactUsFormView(FormView):
    template_name = 'blog_app/contact.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


def like(request, sluq, pk):
    try:
        like = Like.objects.get(article__slug=sluq, user__id=request.user.id)
        like.delete()
        return JsonResponse({'response':'unliked'})
    except:
        Like.objects.create(article_id=pk, user_id=request.user.id)
        return JsonResponse({'response': 'liked'})