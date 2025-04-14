from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse


from accounts.models import Profile
from .models import Post
from .forms import PostForm


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


def redirectFBV(request):
    """
    redirect by function base view
    """
    return redirect('https://www.itmeter.ir')


class RedirectCBV(RedirectView):
    url = "https://www.itmeter.ir"
    

class PostListView(PermissionRequiredMixin ,LoginRequiredMixin, ListView): # it's different with class PostListView(ListView, LoginRequiredMixin):
    permission_required = 'blog.view_post'
    model = Post # OR queryset = Post.objects.all() OR def get_queryset(self)
    context_object_name = 'posts'
    # paginate_by = 2
    ordering = "-id"
    
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True).order_by('-id')
    #     return posts
        

class PostDetailView(DetailView):
    model = Post
    

class PostCreateFormView(FormView):
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/blog/post/"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        

class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content", "status", "category", "published_date"] # or form_class = PostForm
    success_url	= reverse_lazy('blog:post-list') # or  success_url	= '/blog/post/'

    def form_valid(self, form):        
        # form.instance.author = self.request.user
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url	= '/blog/post/'
    

class PostDeleteView(DeleteView):
    model = Post
    success_url	= '/blog/post/'


def post_list_view(request):
    return HttpResponse("ok")

"""
@api_view()
def api_post_list_view(request):
    return Response({"Name":"Poorya"})
"""


