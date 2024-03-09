from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm

# Create your views here.

menu = [{'id': 'users:login', 'name': 'Войти'},
        {'id': 'users:reg', 'name': 'Зарегистрироваться'}]


class LoginUser(LoginView):
    template_name = 'login.html'
    form_class = LoginUserForm
    extra_context = {
        'title': 'Авторизация',
        'page': 'users:login',
    }

    def get_success_url(self):
        return reverse('home')


class RegUser(CreateView):
    template_name = 'register.html'
    form_class = RegisterUserForm
    extra_context = {
        'title': 'Регистрация',
        'page': 'users:reg',
    }

    def get_success_url(self):
        return reverse('users:login')


@login_required
def logout_user(request):
    logout(request)
