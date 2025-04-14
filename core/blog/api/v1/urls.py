from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from . import views

app_name = "api-v1"

urlpatterns = [
    path('post/', views.api_post_list, name='api-post-list'),
    path('post/<int:id>/detail/', views.api_post_detail, name='api-post-detail'),
    
]