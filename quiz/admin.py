from django.contrib import admin
from quiz.models import QuizApp,QuizAppAnswer,QuizAppCategory,QuizAppQuestion
import nested_admin
class QuizAppAnswerTabularInline(nested_admin.NestedTabularInline):
    model = QuizAppAnswer
    extra = 0
class QuizAppQuestionAdmin(admin.ModelAdmin):
    model = QuizAppQuestion
    inlines = [QuizAppAnswerTabularInline]
    extra = 1


admin.site.register(QuizApp)
admin.site.register(QuizAppCategory)
admin.site.register(QuizAppQuestion, QuizAppQuestionAdmin)
admin.site.register(QuizAppAnswer)


