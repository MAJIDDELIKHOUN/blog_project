from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime
from django.utils.html import format_html


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=70, verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    slug = models.SlugField(null=True, unique=True, verbose_name='ادرس')

    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return f'{self.title}'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()

    def get_absolute_url(self):
        return reverse('blog_app:category_detail', args=[self.slug])


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='article',
                               verbose_name='نویسنده')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته بندی')
    title = models.CharField(max_length=70, verbose_name='عنوان')
    body = models.TextField(verbose_name='متن')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='بروزرسانی')
    pub_date = models.DateField(auto_now=True, verbose_name='تاریخ انتشار')
    slug = models.SlugField(null=True, unique=True, blank=True, verbose_name='آدرس')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def showimage(self):
        return format_html(f'<img src="{self.image.url}" width="50px" height="50px">')

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog_app:article_detail', args=[self.slug])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True,
                               verbose_name='والد')
    email = models.EmailField(verbose_name='ایمیل')
    body = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'{self.user}-{self.body[:20]}'


class Contact_Us(models.Model):
    name = models.CharField(max_length=70, verbose_name='نام')
    subject = models.CharField(max_length=70, verbose_name='موضوع')
    email = models.EmailField(verbose_name='ایمیل')
    body = models.TextField(verbose_name='متن')
    created_at = models.DateTimeField(default=datetime.now(), verbose_name='تاریخ انتشار')

    class Meta:
        verbose_name = 'نظرات'
        verbose_name_plural = 'ارتباط با ما'

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='liles', verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
        ordering=('-created_at',)