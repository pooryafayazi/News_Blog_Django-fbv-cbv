from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Post


def indexView(request):
    """
    a function based view to show index page
    """
    context = {"name": 'function base view'}
    return render(request, 'index.html', context)



class IndexTemplateView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        # Call (TemplateView) the superclass' method to get_context_data for creating an object which is named context
        context = super().get_context_data(**kwargs)
        context['name'] = 'custum class-based view'
        context['post'] = Post.objects.all()
        return context