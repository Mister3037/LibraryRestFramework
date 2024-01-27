from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from rest_framework import generics, status


# Create your views here.


# class BookListApiView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
#
# class RetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class ListAPIView(APIView):


    def get(self, request):
        model = Book.objects.all()
        serializers = BookSerializer(model, many=True).data

        content = {
            "status": True,
            "content": serializers
        }
        return Response(content)



class DetailAPIView(APIView):


    def get(self, request, pk):
        data = Book.objects.get(id=pk)
        serializers = BookSerializer(data).data

        content = {
            "status": True,
            "content": serializers
        }
        return Response(content)



class CreateAPIView(APIView):


    def post(self, request):
        information = request.data



