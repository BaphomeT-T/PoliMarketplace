from django.db import models

class Sector(models.Model):
    nombre = models.CharField(max_length=100, unique=True)  # Nombre único para cada sector

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Fecha_Nacimiento = models.DateField()
    Sexo = models.CharField(max_length=10, choices=[('male', 'Masculino'), ('female', 'Femenino'), ('other', 'Otro')])
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
    Cedula = models.CharField(max_length=10, unique=True)  
    Contrasenia = models.CharField(max_length=128)  

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"
