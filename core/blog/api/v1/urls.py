from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from . import views

app_name = "api-v1"

urlpatterns = [
    path('post/', views.api_post_list, name='api-post-list'),
    path('post/<int:id>/detail/', views.api_post_detail, name='api-post-detail'),
    
    path('post-apiview/', views.PostListAPIView.as_view(), name='api-post-list-apiview'),
    path('post-apiview/<int:id>/detail/', views.PostDetailAPIView.as_view(), name='api-post-detail-apiview'),
    
    path('post-generics/', views.PostListGenericAPIView.as_view(), name='api-post-list-generics'),
    path('post-generics-mixins/', views.PostListGenericAPIViewMixins.as_view(), name='api-post-list-generics-mixins'),
    path('post-generics-listcreateapiview/', views.PostListGenericsListCreateAPIView.as_view(), name='api-post-list-listcreateapiview'),

    
]