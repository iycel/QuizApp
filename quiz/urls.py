from django.urls import path, include
from quiz.views import QuizAppView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('quiz', QuizAppView)

urlpatterns = [
    path('_nested_admin/', include('nested_admin.urls')),

]

urlpatterns += router.urls 
