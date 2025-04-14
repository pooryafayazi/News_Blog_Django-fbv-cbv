from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from . import views

app_name = "blog"

urlpatterns = [
    path("fbv-index/", views.indexView, name='fbv-index'),
    path("cbv-index/", TemplateView.as_view(template_name='index.html', extra_context={"name": "class base view"}), name='cbv-index'),
    path("cbv-index-custum/", views.IndexTemplateView.as_view(), name='cbv-index-custum'),
    path('go-to-itmeter/', RedirectView.as_view(url='https://itmeter.ir/'), name='go-to-itmeter'),
    path('go-to-index-cbv/', RedirectView.as_view(pattern_name="blog:cbv-index"), name='go-to-cbv-index'),
    
    # custum redirect 
    path('go-to-itmeter-fbv/', views.redirectFBV, name='redirect-fbv'),
    path('go-to-itmeter-cbv/', views.RedirectCBV.as_view(), name='redirect-cbv'),
    
    path('post/', views.PostListView.as_view(), name="post-list"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create-by-formview/', views.PostCreateFormView.as_view(), name='post-create-by-formview'),
    path('post/create-by-creatview/', views.PostCreateView.as_view(), name='post-create-by-creatview'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    
    # 5
    path('post-httpresponse/', views.post_list_view, name='httpresponse-post-list'),
    # path('post-api-view/', views.api_post_list_view, name='api-post-list'),
    
    path('api/v1/', include('blog.api.v1.urls'))
    
]