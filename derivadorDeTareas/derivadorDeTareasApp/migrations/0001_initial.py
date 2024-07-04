# Generated by Django 5.0.6 on 2024-07-04 00:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_set', related_query_name='user', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_set', related_query_name='user', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=254)),
                ('fecha_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_fin', models.DateTimeField()),
                ('prioridad', models.IntegerField()),
                ('urgencia', models.IntegerField()),
                ('numero_tarea', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('no iniciado', 'No Iniciado'), ('en progreso', 'En Progreso'), ('en espera', 'En Espera'), ('terminada', 'Terminada')], default='no iniciado', max_length=20)),
                ('tarea_anterior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='siguiente', to='derivadorDeTareasApp.tarea')),
                ('tarea_posterior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anterior', to='derivadorDeTareasApp.tarea')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='derivadorDeTareasApp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='derivadorDeTareasApp.tarea')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='derivadorDeTareasApp.usuario')),
            ],
        ),
    ]
