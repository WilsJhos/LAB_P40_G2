from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Tarea
from .forms import TareaForm

def lista_tareas(request):
    # Obtener parámetros de filtro
    filtro_estado = request.GET.get('estado', '')
    filtro_prioridad = request.GET.get('prioridad', '')
    busqueda = request.GET.get('busqueda', '')
    
    # Query base
    tareas = Tarea.objects.all()
    
    # Aplicar filtros
    if filtro_estado:
        tareas = tareas.filter(estado=filtro_estado)
    if filtro_prioridad:
        tareas = tareas.filter(prioridad=filtro_prioridad)
    if busqueda:
        tareas = tareas.filter(
            Q(titulo__icontains=busqueda) | 
            Q(descripcion__icontains=busqueda)
        )
    
    # Estadísticas
    total_tareas = tareas.count()
    completadas = tareas.filter(estado='completada').count()
    pendientes = tareas.filter(estado='pendiente').count()
    vencidas = tareas.filter(
        fecha_vencimiento__lt=timezone.now(),
        estado__in=['pendiente', 'en_progreso']
    ).count()
    
    context = {
        'tareas': tareas,
        'total_tareas': total_tareas,
        'completadas': completadas,
        'pendientes': pendientes,
        'vencidas': vencidas,
        'filtro_estado': filtro_estado,
        'filtro_prioridad': filtro_prioridad,
        'busqueda': busqueda,
    }
    return render(request, 'tareas/lista_tareas.html', context)

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save()
            messages.success(request, '¡Tarea creada exitosamente!')
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    
    return render(request, 'tareas/form_tarea.html', {
        'form': form,
        'accion': 'Crear'
    })

def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tarea actualizada exitosamente!')
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    
    return render(request, 'tareas/form_tarea.html', {
        'form': form,
        'tarea': tarea,
        'accion': 'Editar'
    })

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, '¡Tarea eliminada exitosamente!')
        return redirect('lista_tareas')
    
    return render(request, 'tareas/confirmar_eliminar.html', {
        'tarea': tarea
    })

def cambiar_estado(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    nuevo_estado = request.POST.get('estado')
    
    if nuevo_estado in dict(Tarea.ESTADOS).keys():
        tarea.estado = nuevo_estado
        if nuevo_estado == 'completada':
            tarea.fecha_completada = timezone.now()
        tarea.save()
        messages.info(request, f'Estado actualizado a {tarea.get_estado_display()}')
    
    return redirect('lista_tareas')