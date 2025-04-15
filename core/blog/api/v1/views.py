from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


from . import serializers
from ...models import Post


@api_view(["Get", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
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
        




