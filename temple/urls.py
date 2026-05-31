from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('comunidad/', views.comunidad, name='comunidad'),
    path('terminos/', views.terminos, name='terminos'),
    path('publicacion/eliminar/<int:publicacion_id>/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('toggle-galeria/<int:publicacion_id>/', views.toggle_galeria, name='toggle_galeria'),
    path('notificacion/leida/<int:notificacion_id>/',views.marcar_notificacion_leida,name='marcar_notificacion_leida'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),

    # Rutas para el panel de administración
    path('admin-panel/evento/crear/', views.crear_evento_admin, name='crear_evento_admin'),
    path('admin-panel/evento/eliminar/<int:evento_id>/', views.eliminar_evento_admin, name='eliminar_evento_admin'),

    path('admin-panel/usuario/eliminar/<int:user_id>/', views.eliminar_usuario_admin, name='eliminar_usuario_admin'),

    path('admin-panel/perfil/aprobar/<int:perfil_id>/', views.aprobar_cinturon_admin, name='aprobar_cinturon_admin'),
    path('admin-panel/perfil/rechazar/<int:perfil_id>/', views.rechazar_cinturon_admin, name='rechazar_cinturon_admin'),

    path('admin-panel/publicacion/eliminar/<int:publicacion_id>/', views.eliminar_publicacion_admin, name='eliminar_publicacion_admin'),

]