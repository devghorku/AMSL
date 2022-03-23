from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from AMSL.serializers import UserSerializer


def index(request):
    return render(request, 'index.html')


def access_forbiden(request):
    return render(request, './errors/403.html')


def page_not_found(request):
    return render(request, './errors/404.html')


class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)