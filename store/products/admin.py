from django.contrib import admin
from .models import Category, Item

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "sub_category", "is_deleted")
    list_filter = ("is_deleted",)
    search_fields = ("category_name",)
    ordering = ("is_deleted", "category_name")
    autocomplete_fields = ("sub_category",)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "final_price", "stock", "created_at")
    list_filter = ("is_deleted", "category")
    search_fields = ("item_name",)
    ordering = ("-created_at", "name")
    autocomplete_fields = ("category",)