from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {'name': 'Ambroise BAZIE'}
    return render(request, 'users/index.html', context)
