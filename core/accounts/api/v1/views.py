from rest_framework import generics, status
from rest_framework.response import Response


from .serializers import RegistraionSerializer

class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistraionSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegistraionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email': serializer.validated_data['email']
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        