from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken 

from . import views

app_name = "api-v1"

urlpatterns = [
    # registration
    path('registration/', views.RegistrationAPIView.as_view(), name='registration'),
    path('token/login/', ObtainAuthToken.as_view(), name='token-login'),
    path('token-custom/login/', views.CustomObtainAuthToken.as_view(), name='token-custom-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout')
    
    # change password
    
    # reset password
    
    # login token
    
    # login jwt
    
    
]