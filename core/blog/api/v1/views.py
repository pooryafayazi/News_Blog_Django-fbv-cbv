from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def api_post_list(request):
    return Response({"Name":"Poorya"})


@api_view()
def api_post_detail(request, id):
    return Response(id)






