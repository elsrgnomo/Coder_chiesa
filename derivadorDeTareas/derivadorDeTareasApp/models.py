import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email válido')
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, apellido=apellido)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, apellido, password):
        user = self.create_user(email, nombre, apellido, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    id_unico = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_usuario_set',  # Nombre de relación inversa personalizado
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='custom_usuario',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_usuario_set',  # Nombre de relación inversa personalizado
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_usuario',
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']


    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    @property
    def is_staff(self):
        return self.is_admin

class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('no iniciado', 'No Iniciado'),
        ('en progreso', 'En Progreso'),
        ('en espera', 'En Espera'),
        ('terminada', 'Terminada'),
    ]

    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=254)
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_fin = models.DateTimeField()
    prioridad = models.IntegerField()
    urgencia = models.IntegerField()
    tarea_anterior = models.ForeignKey('self', related_name='siguiente', on_delete=models.SET_NULL, null=True, blank=True)
    tarea_posterior = models.ForeignKey('self', related_name='anterior', on_delete=models.SET_NULL, null=True, blank=True)
    numero_tarea = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='no iniciado')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas')

    def __str__(self):
        return self.nombre
    
class Comentario(models.Model):
    tarea = models.ForeignKey(Tarea, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comentario de {self.usuario} en {self.tarea}'
    