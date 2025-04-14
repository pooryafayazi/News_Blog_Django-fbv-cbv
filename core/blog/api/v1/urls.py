from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from . import views

app_name = "api-v1"

urlpatterns = [

    # 5
    path('post/', views.api_post_list_view, name='api-post-list'),    

    
]