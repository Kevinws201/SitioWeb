from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# models.py

class CustomUser(AbstractUser):
    CARRERA_CHOICES = [
        ("Sistemas Computacionales","ISC"),
        ("Informática","II"),
        ("TICS","ITICS", ),
        ("Industrial","II"),
    ]

    NIVEL_EDUCATIVO_CHOICES = [
        ("LIC", "Licenciatura/Ingeniería"),
        ("POS", "Posgrado"),
    ]
    email = models.EmailField(unique=True,null=True)
    carrera = models.CharField(max_length=50, choices=CARRERA_CHOICES,null=True)
    nivel_educativo = models.CharField(max_length=5, choices=NIVEL_EDUCATIVO_CHOICES,null=True)
    semestre = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
