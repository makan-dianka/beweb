from . import views
from django.urls import path

app_name = 'vote'

urlpatterns = [
    path('', views.home, name="home"),
    path('vote/', views.vote, name="vote"),
    path('successful/<str:name>/', views.success, name="success"),
    path('scrutin/', views.scrutin, name="scrutin"),
    path('voteurs/', views.voteurs, name="voteurs"),
]