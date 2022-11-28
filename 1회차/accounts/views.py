from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
