from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('home', views.home_page, name='home'),
    path('notes', views.notes, name='notes'),
    path('add_note', views.AddNote.as_view(), name='add_note'),
]