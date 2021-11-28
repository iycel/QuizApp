from django.shortcuts import render
from quiz.models import QuizApp, QuizAppAnswer, QuizAppCategory, QuizAppQuestion
from rest_framework import permissions, viewsets
from quiz.serializers import QuizAppCategorySerializers, QuizAppQuestionSerializers, QuizAppSerializers
# from quiz.permissions import IsStaffOrReadOnly

# class QuizAppView(viewsets.ModelViewSet):
#     queryset = QuizApp.objects.all()
#     serializer_class = QuizAppSerializers
    # permission_classes = (IsStaffOrReadOnly)
class CategoryList(viewsets.ModelViewSet):
    queryset = QuizAppCategory.objects.all()
    serializer_class = QuizAppCategorySerializers

class QuizAppView(viewsets.ModelViewSet):
    queryset = QuizApp.objects.all()
    serializer_class = QuizAppSerializers

class QuiazAppQuestionView(viewsets.ModelViewSet):
    queryset = QuizAppQuestion.objects.all()
    serializer_class = QuizAppQuestionSerializers


