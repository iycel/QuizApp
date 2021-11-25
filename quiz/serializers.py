from rest_framework import serializers
from quiz.models import QuizApp, QuizAppAnswer, QuizAppCategory, QuizAppQuestion

class QuizAppSerializers(serializers.ModelSerializer):
    class Meta :
        model = QuizApp
        fields = '__all__'