from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import RegisterSerializer

class RegisterApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # Hangi serializeri belirtmişske class ımızda o serializeri döndürüyor ( RegisterSerializer)
        # serializer = RegisterSerializer(data=request.data)   # buda olabilir
        serializer.is_valid(raise_exception=True)  # valid değilse hata döndür diye bir seçenek ekleyebiliyoruz raise_exception=True
        serializer.save()
        return Response({
            'message' : 'User successfully created'
        })

