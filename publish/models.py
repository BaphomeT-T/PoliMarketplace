from django.db import models
from django.conf import settings

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria


class Estado(models.Model):
    nombre_estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_estado

class Producto(models.Model):
    VENTA_ESTADO_CHOICES = [
        ('EnVenta', 'En venta'),
        ('Vendido', 'Vendido'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    venta_estado = models.CharField(max_length=20, choices=VENTA_ESTADO_CHOICES, default='EnVenta')

    def save(self, *args, **kwargs):
        if not self.sector and self.usuario:
            self.sector = self.usuario.sector
        print(f"Guardando producto: {self.titulo}")
        super().save(*args, **kwargs)
        print(f"Producto guardado con ID: {self.id}")


class Imagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='imagenes_producto/')

    def __str__(self):
        return f"Imagen de {self.producto.titulo}"
