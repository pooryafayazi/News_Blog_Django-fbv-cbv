from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


from . import serializers
from ...models import Post


@api_view()
def api_post_list(request):
    return Response({"Name":"Poorya"})


@api_view()
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

    post = get_object_or_404(Post, pk=id)
    serializer = serializers.PostSerializer(post)
    return Response(serializer.data)





