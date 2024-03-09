from django import template

register = template.Library()

menu = [
    {'id': 'home', 'name': 'Главная'},
    {'id': 'notes', 'name': 'Заметки'},
    {'id': 'add_note', 'name': 'Создать заметку'},
]


@register.simple_tag()
def main_menu():
    return menu
