from django.contrib import admin
from quiz.models import QuizApp,QuizAppAnswer,QuizAppCategory,QuizAppQuestion

admin.site.register(QuizApp)
admin.site.register(QuizAppCategory)
admin.site.register(QuizAppQuestion)
admin.site.register(QuizAppAnswer)

