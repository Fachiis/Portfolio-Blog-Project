from django.contrib import admin

from .models import Blog


class CustomBlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ('title', 'pub_date',)

admin.site.register(Blog, CustomBlogAdmin)
        
    



