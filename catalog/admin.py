from django.contrib import admin
from .models import Product, Category

# Register your models here.
'''admin.site.register(Product)
admin.site.register(Category)'''


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category',)
    list_filter = ('price',)
    search_fields = ('title', 'description',)
    actions = ('delete_selected',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_filter = ('title',)
    search_fields = ('title', 'description',)
    actions = ('delete_selected',)
