from django.db import models

class TipoComida(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='tipos/', blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de Comida'
        verbose_name_plural = 'Tipos de Comida'


class Restaurante(models.Model):
    tipo_comida = models.ForeignKey(TipoComida, on_delete=models.CASCADE, related_name='restaurantes')
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='restaurantes/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'