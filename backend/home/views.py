from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import BlogPost, Image

# DEBUGGING 
#class HomeView(TemplateView):
#    template_name = "base.html"
#
#    def get_context_data(self, **kwargs):
#        """Testing"""
#        context = super(HomeView, self).get_contest_data(**kwargs)
#        context['posts'] = BlogPost.objects.all() 
#        return context 

def home_view(request):
    """View images/thumbnails on home page"""
    posts = BlogPost.objects.all()
    return render(request, 'base.html', {'posts':posts})

def detail_view(request, id): 
    """Display slideshow and details of imageset collection"""
    post = get_object_or_404(BlogPost, id=id)
    photos = Image.objects.filter(posts=post)
    return render(request, 'detail.html', { 
        'post':post,
        'photos':photos
        })
