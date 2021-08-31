from django.shortcuts import render


def Home(request):

    context = {
        'titulo': 'Quiz Chaco - Inicio'
    }

    return render(request, 'index.html', context)
