from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()

    def get_absolute_url(self):
        return reverse('blog_app:category_detail', args=[self.slug])


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='article')
    category = models.ManyToManyField(Category, related_name='articles')
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(auto_now=True)
    slug = models.SlugField(null=True, unique=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog_app:article_detail', args=[self.slug])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}-{self.body[:20]}'


class Contact_Us(models.Model):
    name=models.CharField(max_length=70)
    subject=models.CharField(max_length=70)
    email=models.EmailField()
    body=models.TextField()

    def __str__(self):
        return self.name







