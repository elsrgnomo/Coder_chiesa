# Gestión de Tareas con Django

## Nombre del Proyecto
Gestión de Tareas

## Objetivo Funcional
Esta aplicación permite la gestión de tareas con roles diferenciados para usuarios y administradores.

## Descripción de Modelos

### Usuario
- `nombre`
- `apellido`
- `email`
- `password`
- `is_admin`

### Tarea
- `nombre`
- `descripcion`
- `fecha_inicio`
- `fecha_fin`
- `prioridad`
- `urgencia`
- `tarea_anterior`
- `tarea_posterior`
- `numero_tarea`
- `estado`
- `usuario`

### Comentario
- `tarea`
- `usuario`
- `comentario`
- `fecha`

## Acceso al Panel de Administración
- **Usuario**: admin
- **Contraseña**: adminpassword
