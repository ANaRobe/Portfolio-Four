from django.contrib import admin
from .models import Cocktail, Remark
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Cocktail)
class CocktailAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('status', 'publish_date')
    summernote_fields = ('ingredients', 'steps')
    list_display = ('title', 'slug', 'status', 'publish_date')
    search_fields = ['title', 'ingredients']


@admin.register(Remark)
class RemarkAdmin(admin.ModelAdmin):
    list_display = ('cocktail', 'user', 'text', 'publish_date')
    list_filter = ('publish_date',)
