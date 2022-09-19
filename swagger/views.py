from django.shortcuts import render

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .open_api_params import get_params, post_params
from .serializer import GetRequestSerializer, GetResponseSerializer, PostRequestSerializer, PostResponseSerializer


class View(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(manual_parameters=get_params)
    def get(self, request):
        return Response("Swagger 연동 테스트")

    @swagger_auto_schema(request_body=post_params)
    def post(self, request):
        return Response("Swagger Schema")

class SerializerView(APIView):
    permission_classes = [permissions.AllowAny]
    @swagger_auto_schema(query_serializer=GetRequestSerializer, responses={"200":GetResponseSerializer})
    def get(self, request):
        return Response("Swagger 연동 테스트")

    @swagger_auto_schema()
    def post(self, request):
        return Response("Swagger Schema")

    @swagger_auto_schema(request_body=PostRequestSerializer, responses={"201": PostResponseSerializer})
    def post(self, request):
        return Response("Swagger Schema")