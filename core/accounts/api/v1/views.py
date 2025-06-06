from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from mail_templated import send_mail, EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError

from django.conf import settings

from . import serializers
from ...models import User, Profile
from ..utils import EmailThread

class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = serializers.RegistraionSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = serializers.RegistraionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            data = {
                'email': email
            }
            user_obj = get_object_or_404(User, email = email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/activation.tpl', {'token': token}, 'admin@admin.com', to=[email])
            EmailThread(email_obj).start()
            return Response(data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
        

class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = serializers.CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer


class ChangePasswordAPIView(generics.GenericAPIView):
    serializer_class = serializers.ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated]
    
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def put(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                return Response({'details':'password changed successfully.'}, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset= Profile.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj    


class TestEmailSend(generics.GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        self.email = "poorya2@poorya2.com"
        user_obj = get_object_or_404(User, email = self.email)
        # send_mail('email/send_mail.tpl', {'name': 'poorya'}, 'admin@admin.com', [self.email])
        
        token = self.get_tokens_for_user(user_obj)
        
        email_obj = EmailMessage('email/send_mail.tpl', {'token': token}, 'admin@admin.com', to=[self.email])
        EmailThread(email_obj).start()
        
        return Response('email sent.')    

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ActivationApiView(APIView):
    
    def get(self, request, token, *args, **kwargs):
        # print(token)
        try:
            token = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            user_id = token.get("user_id")
        except ExpiredSignatureError:
            return Response({'details':'the token has been expired!'}, status=status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError:
            return Response({'details':'the token is invalid!'}, status=status.HTTP_400_BAD_REQUEST)
        user_obj = User.objects.get(pk=user_id)
        
        if user_obj.is_verified:
            return Response({'details': 'your account has already been verified!'}) 
                
        user_obj.is_verified = True
        user_obj.save()
        return Response({'details': 'your account has been verified successfully.'}) 


class ActivationResendApiView(generics.GenericAPIView):
    serializer_class = serializers.ActivationResendSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data['user'] 
        token = self.get_tokens_for_user(user_obj)
        email_obj = EmailMessage('email/activation.tpl', {'token': token}, 'admin@admin.com', to=[user_obj.email])
        EmailThread(email_obj).start()
        return Response({'details':'user activation resend successfully.'},status=status.HTTP_200_OK)
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)