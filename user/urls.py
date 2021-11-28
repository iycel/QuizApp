from django.urls import path, include
from .views import RegisterApi

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', RegisterApi.as_view(), name='register'),
]
