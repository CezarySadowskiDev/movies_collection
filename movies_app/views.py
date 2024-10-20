from django.shortcuts import render


def index(request):
    return render(request, "movies_app/index.html")