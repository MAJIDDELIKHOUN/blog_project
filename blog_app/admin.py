from django.contrib import admin
from .models import Article, Category, Comment, Contact_Us,Like


# Register your models here.
class Commentinline(admin.TabularInline):
    model = Comment
@admin.register(Article)
class Articleadmin(admin.ModelAdmin):
    list_display = ('title', 'author','showimage')
    list_filter = ('pub_date',)
    search_fields = ('title', 'body')
    inlines = (Commentinline,)


@admin.register(Contact_Us)
class Contact_Usadmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    search_fields = ('name',)


@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    list_display = ('user', 'article')
    list_filter = ('created_at',)
    search_fields = ('user',)

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    search_fields = ('title',)

@admin.register(Like)
class Liceadmin(admin.ModelAdmin):
    list_display = ('user','article')
