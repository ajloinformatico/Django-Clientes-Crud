from django.db import models


# Create your models here.
# Se debe importar siempre models
class Persona(models.Model):
    # Si no se coloca clabe primaria django coloca una por defecto auto-incrementada que se va a llamar pk
    id = models.AutoField(primary_key=True)  # La primera hace referencia al tipo de dato y la segunda al campo
    # CAMPO AUTOINCREMENTADO
    nombre = models.CharField(max_length=100) # cadena campo VARCHAR MAX 100
    apellido = models.CharField(max_length=120) # VARCHAR MAX 120
    correo = models.EmailField(max_length=200) # Correo electrónico

    def __str__(self):
        return str(self.id) + " " + str(self.nombre)+ " " +str(self.apellido) + " " + str(self.correo)

