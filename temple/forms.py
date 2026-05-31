from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil, HistoriaDojo


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    apodo = forms.CharField(required=False)

    color_cinturon = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Selecciona tu cinturón'),
            ('Blanco', 'Blanco'),
            ('Amarillo', 'Amarillo'),
            ('Naranja', 'Naranja'),
            ('Verde', 'Verde'),
            ('Azul', 'Azul'),
            ('Marrón', 'Marrón'),
            ('Negro', 'Negro'),
        ]
    )

    dan = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Sin Dan'),
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

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in [
            'username',
            'email',
            'password1',
            'password2',
            'apodo',
            'color_cinturon',
            'dan'
        ]:
            self.fields[field].widget.attrs.update({
                'class': 'form-control dojo-input'
            })


class PerfilForm(forms.ModelForm):
    rango = forms.ChoiceField(
        choices=[
            ('Alumno', 'Alumno'),
            ('Competidor', 'Competidor'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control dojo-input'
        })
    )

    victorias_amateur = forms.IntegerField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control dojo-input',
            'placeholder': 'Victorias'
        })
    )

    derrotas_amateur = forms.IntegerField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control dojo-input',
            'placeholder': 'Derrotas'
        })
    )

    eliminar_foto = forms.BooleanField(required=False)

    class Meta:
        model = Perfil
        fields = [
            'foto_perfil',
            'biografia',
            'rango',
            'victorias_amateur',
            'derrotas_amateur',
            'banner_perfil',
            'eliminar_foto'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['foto_perfil'].widget.attrs.update({
            'class': 'form-control dojo-input'
        })

        self.fields['biografia'].widget.attrs.update({
            'class': 'form-control dojo-input',
            'placeholder': 'Escribe tu historia como guerrero...'
        })

class HistoriaDojoForm(forms.ModelForm):
    class Meta:
        model = HistoriaDojo
        fields = ['titulo', 'descripcion', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['titulo'].widget.attrs.update({
            'class': 'form-control dojo-input',
            'placeholder': 'Título de tu publicación'
        })

        self.fields['descripcion'].widget.attrs.update({
            'class': 'form-control dojo-input',
            'placeholder': 'Comparte una historia, entrenamiento o logro...'
        })

        self.fields['imagen'].widget.attrs.update({
            'class': 'form-control dojo-input'
        })