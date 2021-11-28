from rest_framework import serializers
from quiz.models import QuizApp, QuizAppAnswer, QuizAppCategory, QuizAppQuestion

class QuizAppCategorySerializers(serializers.ModelSerializer):
    class Meta :
        model = QuizAppCategory
        fields = [
            'id',
            'name',
            'quiz_count'
        ]

class QuizAppSerializers(serializers.ModelSerializer):
    class Meta :
        model = QuizApp
        fields = [
            'title',
            'question_count'
        ]


class QuizAppAnswerSerializers(serializers.ModelSerializer):
    class Meta : 
        model = QuizAppAnswer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]
 
class QuizAppQuestionSerializers(serializers.ModelSerializer):
    answer = QuizAppAnswerSerializers(many=True, read_only=True)
    difficulty = serializers.SerializerMethodField()
    class Meta:
        model = QuizAppQuestion
        fields = [
            "title",
            "answer",
            "difficulty",
        ]
