from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

app_name = "api-v1"

urlpatterns = [
    # registration
    path('registration/', views.RegistrationAPIView.as_view(), name='registration'),
    path('token/login/', ObtainAuthToken.as_view(), name='token-login'),
    path('token-custom/login/', views.CustomObtainAuthToken.as_view(), name='token-custom-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),
    
    # simple jwt
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-token-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-token-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-token-verify'),
    path('jwt-custom/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-token-custom-create'),    
    
    # change password
    path('change-password/', views.ChangePasswordAPIView.as_view(), name='change-password'),
    
    # profile
    path('profile/', views.ProfileAPIView.as_view(), name='profile'),
    
    # activation
    path('test-emailconfirm/', views.TestEmailSend.as_view(), name=''),
    # path('activation/confirm/', views..as_view(), name=''),
    # path('activation/resend/', views..as_view(), name=''),
    
    
    
]