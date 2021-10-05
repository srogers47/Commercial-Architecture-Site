from django.contrib import admin
from .models import BlogPost, Image

class PostImageAdmin(admin.StackedInline):
    model = Image

@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    inlinse = [PostImageAdmin]
    class Meta:
        model = BlogPost

#NOTE: Testing 
@admin.register(Image)
class PostImageAdmin(admin.ModelAdmin):
    pass 

