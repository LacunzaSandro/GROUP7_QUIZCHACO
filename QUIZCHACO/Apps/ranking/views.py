from django.shortcuts import render
from Apps.genericos.models import QuizUsuario


# Create your views here.
def ranking(request):
    # definimos que solo se mostraran los diez primeros de la lista
    total_user_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:10]
    contador = total_user_quiz.count()

    context = {
        'usuario_quiz': total_user_quiz,
        'contar_user': contador,
        'titulo': "Quiz Chaco - Ranking"
    }
    return render(request, 'ranking/ranking.html', context)
