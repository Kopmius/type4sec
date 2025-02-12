from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "t4s"
urlpatterns = [
    path('addmodel/', views.addmodel, name='addmodel'),
    path('join/', views.join, name='join'),
    path('success/', views.index, name='success'),
    path('fail/', views.login, name='loginfail'),
    path('', auth_views.LoginView.as_view(template_name='t4s/login.html'), name='login')
]
