"""
URL configuration for derivadorDeTareasApp

"""
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('menu/', views.menu_principal, name='menu_principal'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('tarea/nueva/', views.nueva_tarea, name='nueva_tarea'),
    path('tarea/<int:pk>/', views.detalle_tarea, name='detalle_tarea'),
    path('tarea/<int:pk>/editar/', views.editar_tarea, name='editar_tarea'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuario/nuevo/', views.registrar_usuario, name='registrar_usuario'),
    path('usuario/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
]
