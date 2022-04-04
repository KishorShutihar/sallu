from django.shortcuts import render
from .models import Actor


def actor(request):
    actors = Actor.objects.all()
    return render(request,'home.html', {'actors':actors})