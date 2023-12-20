from django.contrib import admin
from pages.models import *

@admin.register(MainScrollMode)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'discount', 'created_at', 'updated_at']
    search_fields = ['title', 'info']
    list_filter = ['created_at', 'updated_at']

@admin.register(MainMenuMode)
class ModelNameMenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'discount', 'created_at', 'updated_at']
    search_fields = ['title', 'info']
    list_filter = ['created_at', 'updated_at']