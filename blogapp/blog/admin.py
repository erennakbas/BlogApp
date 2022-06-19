from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Blog,Category
class BlogAdmin(admin.ModelAdmin):
    list_display= ("title", "is_active","slug", "selected_categories")
    list_editable= ("is_active",)
    search_fields= ("title","description")
    readonly_fields= ("slug",)
    list_filter= ("categories","is_active","categories")
    def selected_categories(self, obj):
        html="<ul>"
        for category in obj.categories.all():
            html += "<li>"+category.name+"</li>"    
        return mark_safe(html+"</ul>")
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
