from django import forms
from .models import Tarea, Comentario, Usuario
from django.contrib.auth.forms import UserCreationForm

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'prioridad', 'urgencia', 'tarea_anterior', 'tarea_posterior', 'estado']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'password']

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'password1', 'password2']
