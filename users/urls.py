from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('reg', views.RegUser.as_view(), name='reg'),
    path('logout', views.logout_user, name='logout')
]