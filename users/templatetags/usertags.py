from django import template
from users.views import menu

register = template.Library()


@register.simple_tag()
def user_menu():
    return menu
