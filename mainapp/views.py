from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from mainapp.forms import CreateNote
from mainapp.models import Notes


# Create your views here.

def home_page(request):
    return render(request, 'homepage.html', {'page': request.path[1:]})


@login_required
def notes(request):
    notes = Notes.objects.filter(author=request.user).all()
    context = {
        'title': 'Заметки',
        'page': request.path[1:],
        'notes': notes,
    }
    return render(request, 'notes.html', context)


class AddNote(LoginRequiredMixin, CreateView):
    template_name = 'add_note.html'
    context = {
        'title': 'Добавить заметку',
        'page': 'add_note',
        'form': CreateNote
    }

    def get(self, request):
        return render(request, 'add_note.html', context=AddNote.context)

    def post(self, request):
        form = CreateNote(request.POST)
        if form.is_valid():
            form.instance.author = self.request.user
            form.save()

        return redirect('notes')
