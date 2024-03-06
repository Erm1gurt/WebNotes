from django.shortcuts import render


# Create your views here.

def home_page(request):
    return render(request, 'homepage.html', {'page': request.path})


def notes(request):
    return render(request, 'notes.html', {'page': request.path})


def add_note(request):
    return render(request, 'add_note.html', {'page': request.path})


def register(request):
    user = request.user if not request.user.is_anonymous else ''
    error_massages = []
    context = {'page': request.path, 'massages': error_massages, 'user': user}
    if request.method == 'GET':
        return render(request, 'register.html', context)
    elif request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password1, password2 = data.get('password'), data.get('re_password')
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        is_teacher = bool(data.get('is_teacher'))

        if not username:
            error_massages.append('Имя пользователя не указано')
        if not password1 or not password2 or password1 != password2:
            error_massages.append('Пароль не указан или пароли не совпадают')
        if not email:
            error_massages.append('Электронная почта не указана')
        if not first_name:
            error_massages.append('Имя не указано')
        if not last_name:
            error_massages.append('Фамилия не указана')
        if User.objects.filter(username=username):
            error_massages.append('Имя пользователя занято')

        if error_massages:
            return render(request, 'register.html', context)
        else:
            new_user = User()
            new_user.create_user(username, password1, email, first_name, last_name, is_teacher)
            return redirect('login')

def register2(request):
    form = RegisterUserForm()
    context = {'page': request.path, 'form': form}
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = User()
            user.create_user(**form.cleaned_data)
            return redirect('home')

    return render(request, 'register.html', context)


def login_page(request):
    user = request.user if not request.user.is_anonymous else ''
    form = LoginUserForm()
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user and user.is_active:
                login(request, user)
                return redirect('home')

            form.add_error(None, 'Пользователь с таким логином и паролем не найден')

    context = {'page': request.path, 'form': form, 'user': user}
    return render(request, 'login.html', context)


def logout(request):
    pass
