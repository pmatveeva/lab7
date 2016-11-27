from django.contrib import admin
from django.contrib import admin
from .models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
    def number_of_items(self, request):
        data = Item.objects.filter(category_id=request.id).all()
        i = len(data)
        return i
    list_display = ('name', 'number_of_items')
    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category')
    list_filter = ['category']
    search_fields = ['code', 'name']

admin.site.register(Item,ItemAdmin)


