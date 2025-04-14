from rest_framework.decorators import api_view
from rest_framework.response import Response


from . import serializers
from ...models import Post


@api_view()
def api_post_list(request):
    return Response({"Name":"Poorya"})


@api_view()
def api_post_detail(request, id):
    post = Post.objects.get(pk=id)
    # print(post.__dict__) # it's a ModelState object
    serializer = serializers.PostSerializer(post)
    # print(serializer.__dict__)
    # print(serializer.data)
    return Response(serializer.data)






