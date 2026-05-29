from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistroForm, PerfilForm, HistoriaDojoForm
from .models import Perfil, HistoriaDojo,Evento

import json
from django.http import JsonResponse


def index(request):
    eventos = Evento.objects.filter(activo=True)

    fotos_galeria = HistoriaDojo.objects.filter(
    mostrar_galeria=True
    ).select_related('autor').order_by('-fecha_creacion')[:6]

    
    planes = [
        {
            'nombre': 'Iniciación',
            'precio': '$35.000',
            'descripcion': 'Para empezar tu camino',
            'frecuencia': '2 veces por semana',
            'beneficios': [
                'Entrenamientos 2 veces por semana',
                'Primera clase de prueba GRATIS',
                'Acceso a solo 1 disciplina (Kudo o Kickboxing)',
                
            ],
            'destacado': False
        },
        {
            'nombre': 'Guerrero',
            'precio': '$45.000',
            'descripcion': 'Para los comprometidos',
            'frecuencia': '3 veces por semana',
            'beneficios': [
                'Entrenamientos 3 veces por semana',
                'Primera clase de prueba GRATIS',
                'Accseso a ambas disciplinas (Kudo y Kickboxing)',
                'Posibilidad de participar en torneos',
                
            ],
            'destacado': True
        },
        {
            'nombre': 'Maestro',
            'precio': '$50.000',
            'descripcion': 'Para los élite',
            'frecuencia': '5 veces por semana',
            'beneficios': [
                'Entrenamientos 5 veces por semana',
                'Primera clase de prueba GRATIS',
                'Accseso a ambas disciplinas (Kudo y Kickboxing)',
                'Posibilidad de participar en torneos',
                'Acceso a horario de avanzados'
            ],
            'destacado': False
        },
        {
            'nombre': 'Plan Infantil',
            'precio': '$35.000',
            'descripcion': 'Para los pequeños guerreros',
            'frecuencia': 'Martes y Viernes',
            'beneficios': [
                'Entrenamientos martes y viernes',
                'Primera clase de prueba GRATIS',
                'Programa adaptado para niños',
                'Desarrollo físico y mental',
                'Soporte a padres/tutores'
            ],
            'destacado': False
        },
    ]
    
    
    return render(request, 'temple/index.html', {'eventos': eventos, 'planes': planes,'fotos_galeria': fotos_galeria,})


def terminos(request):
    return render(request, 'temple/terminos.html')



def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            user = form.save()
            Perfil.objects.get_or_create(
            user=user,
            defaults={
                'apodo': form.cleaned_data.get('apodo', ''),
                'color_cinturon_pendiente': form.cleaned_data.get('color_cinturon', ''),
                'dan_pendiente': form.cleaned_data.get('dan', ''),
                'aprobado_por_admin': False,
            }
        )
            login(request, user)
            return redirect('/perfil/')
        else:
            print("ERRORES:", form.errors)

    else:
        form = RegistroForm()

    return render(request, 'temple/registro.html', {
        'form': form
    })

class CustomLoginView(LoginView):
    template_name = 'temple/login.html'


class CustomLogoutView(LogoutView):
    pass



@login_required
def perfil(request):
    perfil_obj, created = Perfil.objects.get_or_create(user=request.user)
    historias = HistoriaDojo.objects.filter(autor=request.user)

    if request.method == 'POST':
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil_obj)
        historia_form = HistoriaDojoForm(request.POST, request.FILES)

        if 'guardar_perfil' in request.POST and perfil_form.is_valid():

            perfil_actualizado = perfil_form.save(commit=False)

            if perfil_form.cleaned_data.get('eliminar_foto'):
                perfil_actualizado.foto_perfil.delete(save=False)
                perfil_actualizado.foto_perfil = None

            perfil_actualizado.save()

            return redirect('perfil')

        if 'subir_historia' in request.POST and historia_form.is_valid():
            historia = historia_form.save(commit=False)
            historia.autor = request.user
            historia.save()
            return redirect('perfil')
    else:
        perfil_form = PerfilForm(instance=perfil_obj)
        historia_form = HistoriaDojoForm()

    return render(request, 'temple/perfil.html', {
        'perfil_form': perfil_form,
        'historia_form': historia_form,
        'historias': historias,
    })


def comunidad(request):
    historias = HistoriaDojo.objects.all()
    return render(request, 'temple/comunidad.html', {'historias': historias})

@login_required
def eliminar_publicacion(request, publicacion_id):
    publicacion = HistoriaDojo.objects.get(
        id=publicacion_id,
        autor=request.user
    )

    if request.method == 'POST':
        if publicacion.imagen:
            publicacion.imagen.delete(save=False)

        publicacion.delete()

    return redirect('perfil')

@login_required
def toggle_galeria(request, publicacion_id):
    publicacion = HistoriaDojo.objects.get(
        id=publicacion_id,
        autor=request.user
    )

    if request.method == 'POST':
        publicacion.mostrar_galeria = not publicacion.mostrar_galeria
        publicacion.save()

    return redirect('perfil')
# Create your views here.
