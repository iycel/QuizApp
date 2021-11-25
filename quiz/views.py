from django.shortcuts import render
from quiz.models import QuizApp, QuizAppAnswer, QuizAppCategory, QuizAppQuestion
from rest_framework import viewsets
from quiz.serializers import QuizAppSerializers

class QuizAppView(viewsets.ModelViewSet):
    queryset = QuizApp.objects.all()
    serializer_class = QuizAppSerializers

# Create your views here.
