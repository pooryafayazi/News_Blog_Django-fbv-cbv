from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


from . import serializers
from ...models import Post


@api_view(["Get", "POST"])
@permission_classes([IsAuthenticated])
def api_post_list(request):
    if request.method == "GET":        
        posts = Post.objects.filter(status=True)
        serializer = serializers.PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = serializers.PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(["Get", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def api_post_detail(request, id):
    # try:
        # post = Post.objects.get(pk=id)
        # print(post.__dict__) # it's a ModelState object
        # serializer = serializers.PostSerializer(post)
        # print(serializer.__dict__)
        # print(serializer.data)
        # return Response(serializer.data)
    # except Post.DoesNotExist:
        # return Response({"detail": "post does not exist!"}, status=status.HTTP_404_NOT_FOUND)
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":        
        serializer = serializers.PostSerializer(post)
        return Response(serializer.data)    
    elif request.method == "PUT":
        serializer = serializers.PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed successfuly"}, status=status.HTTP_204_NO_CONTENT)



from rest_framework.views import APIView


class PostListAPIView (APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PostSerializer
    def get(self, request):
        posts = Post.objects.filter(status=True)
        serializer = serializers.PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.PostSerializer
    
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail":"item removed successfuly"}, status=status.HTTP_204_NO_CONTENT)



from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins



class PostListGenericAPIView (GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PostSerializer        
    queryset = Post.objects.filter(status=True)
    def get(self, request):
        queryset = self.get_queryset()
        serializer = serializers.PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class PostListGenericAPIViewMixins (GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.filter(status=True)
          
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostListGenericsListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.filter(status=True)
    

class PostDetailGenericAPIView(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,  mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.filter(status=True)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostDetailGenericRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.filter(status=True)
