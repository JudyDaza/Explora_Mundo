# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.URLField()
    precio_base = models.IntegerField(validators=[MinValueValidator(0)])
    duracion_recomendada = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

class Paquete(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField(validators=[MinValueValidator(0)])
    duracion = models.CharField(max_length=50)
    incluye = models.TextField(help_text="Separar por comas los servicios incluidos")
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def servicios_incluidos(self):
        return [s.strip() for s in self.incluye.split(",")]
    
    def __str__(self):
        return f"{self.nombre} - {self.destino.nombre}"

class Reserva(models.Model):
    ESTADOS = [
        ('PEND', 'Pendiente'),
        ('CONF', 'Confirmada'),
        ('CANC', 'Cancelada'),
        ('COMP', 'Completada')
    ]
    
    paquete = models.ForeignKey(Paquete, on_delete=models.PROTECT)
    cliente_nombre = models.CharField(max_length=100)
    cliente_email = models.EmailField()
    cliente_telefono = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cantidad_personas = models.IntegerField(validators=[MinValueValidator(1)])
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=4, choices=ESTADOS, default='PEND')
    notas = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Reserva #{self.id} - {self.paquete.nombre}"