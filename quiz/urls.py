from django.urls import path, include
from quiz.views import QuiazAppQuestionView, QuizAppView, CategoryList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('quiz', QuizAppView)
router.register('category', CategoryList)
router.register('questions', QuiazAppQuestionView)



urlpatterns = [
    path('_nested_admin/', include('nested_admin.urls')),
]

urlpatterns += router.urls 
