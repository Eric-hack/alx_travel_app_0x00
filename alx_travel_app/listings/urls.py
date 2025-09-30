from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def hello(request):
    return Response({"message": "Welcome to Listings API"})

urlpatterns = [
    path('', hello),
]
