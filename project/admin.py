from django.contrib import admin
from .models import Category, Material, Size, Brand, Color, Product, Review

admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(Review)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)#строка поиска

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'material',  'brand',)
    search_fields = ('name', 'category_name')
    list_filter = ('category', )
