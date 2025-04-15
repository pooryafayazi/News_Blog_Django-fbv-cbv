from django.urls import path, include

from . import views

app_name = "api-v1"

urlpatterns = [
    path('post/', views.api_post_list, name='api-post-list'),
    path('post/<int:id>/', views.api_post_detail, name='api-post-detail'),
    
    path('post-apiview/', views.PostListAPIView.as_view(), name='api-post-list-apiview'),
    path('post-apiview/<int:id>/', views.PostDetailAPIView.as_view(), name='api-post-detail-apiview'),
    
    path('post-generics/', views.PostListGenericAPIView.as_view(), name='api-post-list-generics'),
    path('post-generics-mixins/', views.PostListGenericAPIViewMixins.as_view(), name='api-post-list-generics-mixins'),
    path('post-generics-listcreateapiview/', views.PostListGenericsListCreateAPIView.as_view(), name='api-post-list-listcreateapiview'),
    path('post-generics/<int:pk>/', views.PostDetailGenericAPIView.as_view(), name='api-post-detail-generics'),
    path('post-generics-allfunction/<int:pk>/', views.PostDetailGenericRetrieveUpdateDestroyAPIView.as_view(), name='api-post-detail-generics-allfunction'),

    path('post-viewset/', views.PostViewSet.as_view({'get':'list', 'post':'create'}), name='post-viewset'),
    path('post-viewset/<int:pk>/', views.PostViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name='post-viewset'),
    # path('', include(router.urls))
]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', views.PostViewSet, basename='post')
urlpatterns = router.urls # All urls created automatically
