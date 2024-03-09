from django.shortcuts import render


# Create your views here.

def home_page(request):
    print(request.path[1:])
    return render(request, 'homepage.html', {'page': request.path[1:]})


def notes(request):
    return render(request, 'notes.html', {'page': request.path[1:]})


def add_note(request):
    return render(request, 'add_note.html', {'page': request.path[1:]})
