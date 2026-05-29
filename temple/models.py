from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    apodo = models.CharField(max_length=100, blank=True)

    color_cinturon = models.CharField(
        max_length=50,
        blank=True,
        choices=[
            ('Blanco', 'Blanco'),
            ('Amarillo', 'Amarillo'),
            ('Naranja', 'Naranja'),
            ('Verde', 'Verde'),
            ('Morado', 'Morado'),
            ('Marrón', 'Marrón'),
            ('Negro', 'Negro'),
        ]
    )

    color_cinturon_pendiente = models.CharField(
    max_length=20,
    blank=True
    )
    dan_pendiente = models.CharField(max_length=20, blank=True)
    aprobado_por_admin = models.BooleanField(
        default=False
    )
    

    foto_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    biografia = models.TextField(blank=True)
    rango = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if self.aprobado_por_admin and self.color_cinturon_pendiente:
            self.color_cinturon = self.color_cinturon_pendiente
            self.dan = self.dan_pendiente
            self.color_cinturon_pendiente = ''
            self.dan_pendiente = ''

        super().save(*args, **kwargs)
        
    dan = models.CharField(
    max_length=20,
    blank=True,
    choices=[
        ('Sin Dan', 'Sin Dan'),
        ('1° Dan', '1° Dan'),
        ('2° Dan', '2° Dan'),
        ('3° Dan', '3° Dan'),
        ('4° Dan', '4° Dan'),
        ('5° Dan', '5° Dan'),
        ('6° Dan', '6° Dan'),
        ('7° Dan', '7° Dan'),
        ('8° Dan', '8° Dan'),
        ('9° Dan', '9° Dan'),
        ('10° Dan', '10° Dan'),
    ]
)


class HistoriaDojo(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='historias_dojo/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    mostrar_galeria = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
    

class Evento(models.Model):
    titulo = models.CharField(max_length=150)
    fecha = models.CharField(max_length=100)
    lugar = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo

class CombatePactado(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='combates')
    titulo = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='combates/')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.evento.titulo}"
# Create your models here.
