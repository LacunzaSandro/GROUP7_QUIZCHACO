from django.urls import path
from .views import playQuiz

app_name = 'play'

urlpatterns = [
    path('', playQuiz, name='playQuiz'),
]
