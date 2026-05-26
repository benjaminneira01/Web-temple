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
    path('publicacion/galeria/<int:publicacion_id>/',views.toggle_galeria,name='toggle_galeria'),
]