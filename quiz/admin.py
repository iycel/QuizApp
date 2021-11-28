from django.contrib import admin
from quiz.models import QuizApp,QuizAppAnswer,QuizAppCategory,QuizAppQuestion
import nested_admin
class QuizAppAnswerTabularInline(nested_admin.NestedTabularInline):
    model = QuizAppAnswer
    extra = 0
    max_num =5

class QuizAppQuestionAdmin(nested_admin.NestedModelAdmin):
    model = QuizAppQuestion
    inlines = [QuizAppAnswerTabularInline]

# class QuizAppQuestionInline(nested_admin.NestedTabularInline):
#     model = QuizAppQuestion
#     inlines = [QuizAppAnswerTabularInline]
#     extra = 1
#     max_num =10


# class QuizAppAdmin(nested_admin.NestedModelAdmin):
#     model = QuizApp
#     inlines = [QuizAppQuestionInline]


# admin.site.register(QuizApp, QuizAppAdmin)  # Quiz in içerisinden direk soru ve cevaı girebiliriz bu yöntemle
admin.site.register(QuizApp)
admin.site.register(QuizAppCategory)
admin.site.register(QuizAppQuestion, QuizAppQuestionAdmin)
admin.site.register(QuizAppAnswer)


