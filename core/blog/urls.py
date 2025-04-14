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
    path('go-to-itmeter-cbv/', views.RedirectCBV.as_view(), name='redirect-cbv')
]