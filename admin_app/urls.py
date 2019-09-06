from django.contrib import admin
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('create/', ajouterAnnonce, name='create'),
    path('read/', afficherAnnonce, name='read'),
    path('detail/<int:id>', detail, name='detail'),
    path('sign-up/', sign_up, name='sign-up'),
    path('login/', connexion, name='login'),
    path('logout/', deconnexion, name='logout'),
    path('profile/<int:id>', profile, name='profile'),
    path('supprimer/<int:id>', supprimer, name='supprimer'),
    path('modifier/<int:id>', modifier, name='modifier'),
    path('orderby/<str:tri>', orderby, name='orderby'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
