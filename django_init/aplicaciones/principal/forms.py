from django import forms
from .models import Persona


class Personaform(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__' # Todos los campos
        # fields(nomnre, apellido ..) # Para indicar campo a campo
