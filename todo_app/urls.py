from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('excluir/<int:id>/', views.excluir, name='excluir')
]
