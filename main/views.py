from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post


# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()[:2] 
        return context
    