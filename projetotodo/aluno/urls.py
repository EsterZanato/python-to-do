from django.urls import path
from . import views

urlpatterns = [
    path('aluno/', views.minha_view, name='minha_view'),
]