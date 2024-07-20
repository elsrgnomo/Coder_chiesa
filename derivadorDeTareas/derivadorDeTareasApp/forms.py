
from django import forms
from .models import Tarea, Comentario, Usuario
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
# forms.py

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'prioridad', 'urgencia', 'tarea_anterior', 'tarea_posterior', 'estado', 'usuario']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'password', 'avatar']

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'password1', 'password2', 'avatar']

class CambiarContrasenaForm(PasswordChangeForm):
    class Meta:
        model = Usuario
        fields = ['old_password', 'new_password1', 'new_password2']
class GestionUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'avatar']  # Excluyendo campos no editables