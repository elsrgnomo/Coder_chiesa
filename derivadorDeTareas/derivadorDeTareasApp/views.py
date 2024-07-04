from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Tarea, Comentario, Usuario
from .forms import TareaForm, ComentarioForm, UsuarioForm, RegistroUsuarioForm

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu_principal')
        else:
            return render(request, 'login.html', {'error': 'Email o contraseña incorrectos'})
    return render(request, 'login.html')

@login_required
def menu_principal(request):
    if request.user.is_admin:
        return render(request, 'menu_admin.html')
    else:
        return render(request, 'menu_usuario.html')

@login_required
def lista_tareas(request):
    if request.user.is_admin:
        tareas = Tarea.objects.all()
    else:
        tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

@login_required
def detalle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.tarea = tarea
            comentario.save()
            return redirect('detalle_tarea', pk=tarea.pk)
    else:
        form = ComentarioForm()
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea, 'form': form})

@login_required
def nueva_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            return redirect('detalle_tarea', pk=tarea.pk)
    else:
        form = TareaForm()
    return render(request, 'tareas/nueva_tarea.html', {'form': form})

@login_required
def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('detalle_tarea', pk=tarea.pk)
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/editar_tarea.html', {'form': form})

@login_required
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html', {'form': form})

@login_required
def lista_usuarios(request):
    if not request.user.is_admin:
        return redirect('lista_tareas')
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registrar_usuario.html', {'form': form})
