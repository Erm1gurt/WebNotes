from django.shortcuts import render


# Create your views here.

def home_page(request):
    return render(request, 'homepage.html', {'page': request.path})


def notes(request):
    return render(request, 'notes.html', {'page': request.path})


def add_note(request):
    return render(request, 'add_note.html', {'page': request.path})


def register(request):
    pass


def login(request):
    pass


def logout(request):
    pass
