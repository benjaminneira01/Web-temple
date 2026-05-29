from django.contrib import admin
from .models import Perfil, HistoriaDojo,Evento,CombatePactado

admin.site.register(CombatePactado)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'rango')
    search_fields = ('user__username', 'rango')


@admin.action(description="Aprobar cinturón solicitado")
def aprobar_cinturon(modeladmin, request, queryset):
    for perfil in queryset:
        if perfil.color_cinturon_pendiente:
            perfil.color_cinturon = perfil.color_cinturon_pendiente
            perfil.dan = perfil.dan_pendiente
            perfil.color_cinturon_pendiente = ''
            perfil.dan_pendiente = ''
            perfil.aprobado_por_admin = True
            perfil.save()

@admin.register(HistoriaDojo)
class HistoriaDojoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion')
    search_fields = ('titulo', 'autor__username')
    list_filter = ('fecha_creacion',)


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'lugar', 'activo')
    search_fields = ('titulo', 'lugar')
    list_filter = ('activo',)