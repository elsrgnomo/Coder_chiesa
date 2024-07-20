"""
URL configuration for derivadorDeTareasApp

"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('cerrar_sesion/', views.logout_view, name='cerrar_sesion'),
    path('admin-menu/', views.menu_admin, name='menu_admin'),
    path('usuario/menu/', views.menu_usuario, name='menu_usuario'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('tareas/<int:pk>/', views.detalle_tarea, name='detalle_tarea'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:pk>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tareas/<int:pk>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/<int:pk>/', views.detalle_usuario, name='detalle_usuario'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('gestionar_usuario/', views.gestionar_usuario, name='gestionar_usuario'),
    path('cambiar_contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('cambiar_contrasena/done/', views.cambiar_contrasena_done, name='cambiar_contrasena_done'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
]
