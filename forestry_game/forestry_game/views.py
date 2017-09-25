from django.shortcuts import render

from forestry_game.models import CustomUser, Map, Execution

def home ( request ):
    context = dict()
    return render(request, 'index.html', context)
