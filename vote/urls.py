from . import views
from django.urls import path

app_name = 'vote'

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name='register'),
    path('login', views.loginpage, name='loginpage'),
    path('vote/', views.vote, name="vote"),
    path('successful/', views.success, name="success"),
    path('ajout-candidat/', views.ajout, name="ajout"),

    #path('scrutin/', views.scrutin, name="scrutin"),
    #path('voteurs/', views.voteurs, name="voteurs"),
]