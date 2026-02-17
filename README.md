# 📝 Sistema de Gestión de Tareas - Django

¡Bienvenido al **Gestor de Tareas v1.0**! Esta es una aplicación web robusta y elegante desarrollada con **Django** y **PostgreSQL**, diseñada para ayudarte a organizar tus actividades diarias de manera eficiente.

![Estatus del Proyecto](https://img.shields.io/badge/Status-Desarrollo-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-6.0+-darkgreen)
![Tailwind](https://img.shields.io/badge/CSS-Tailwind-blueviolet)

## ✨ Características Principales

- **Dashboard con Estadísticas:** Visualiza rápidamente el total de tareas, completadas, pendientes y vencidas.
- **Gestión Completa (CRUD):** Crea, lee, actualiza y elimina tareas con facilidad.
- **Sistema de Prioridades:** Clasifica tus tareas en **Alta**, **Media** o **Baja** con indicadores visuales de color.
- **Estados Dinámicos:** Cambia el estado de tus tareas entre _Pendiente_, _En Progreso_, _Completada_ o _Cancelada_.
- **Filtros Inteligentes:** Busca por palabra clave y filtra por estado o prioridad para encontrar lo que necesitas.
- **Fechas de Vencimiento:** Controla tus plazos con indicadores de tiempo restante y alertas para tareas vencidas.
- **Interfaz Moderna:** Diseño responsivo y limpio utilizando **Tailwind CSS** y **Font Awesome**.

## 🛠️ Tecnologías Utilizadas

- **Backend:** [Django 6.0](https://www.djangoproject.com/)
- **Base de Datos:** [PostgreSQL](https://www.postgresql.org/)
- **Estilos:** [Tailwind CSS](https://tailwindcss.com/) (vía CDN)
- **Iconos:** [Font Awesome 6.0](https://fontawesome.com/)
- **Tipografía:** Inter (Google Fonts)

## 🚀 Instalación y Configuración

Sigue estos pasos para poner en marcha el proyecto en tu entorno local:

### 1. Requisitos Previos

- Python 3.10+
- PostgreSQL instalado y corriendo.
- Git (opcional).

### 2. Clonar y Preparar el Entorno

```bash
# Clonar el proyecto
git clone <url-del-repositorio>
cd LAB_P40_G2

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
.\Scripts\activate
# En Linux/macOS:
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos

Crea una base de datos en PostgreSQL llamada `tareas_db` y asegúrate de que el archivo `tareas_project/tareas_project/settings.py` tenga tus credenciales:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tareas_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Migraciones y Ejecución

```bash
# Entrar a la carpeta del proyecto Django
cd tareas_project

# Aplicar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

Visita `http://127.0.0.1:8000` para empezar a usar la aplicación.

## 📂 Estructura del Directorio

- `tareas/`: Aplicación de Django con la lógica principal (Modelos, Vistas, Templates).
- `tareas_project/`: Configuración del núcleo del proyecto.
- `requirements.txt`: Archivo de dependencias para `pip`.
- `db.sqlite3`: Base de datos local (solo para pruebas rápidas).

---

Desarrollado con ❤️ por el equipo del Lab P40 G2.
