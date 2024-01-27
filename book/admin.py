from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle', 'author', 'price']
