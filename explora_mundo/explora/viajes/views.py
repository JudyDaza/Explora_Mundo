

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Destino, Paquete

def inicio(request):
    destinos = Destino.objects.all()
    return render(request, 'sitio/inicio.html', {'destinos': destinos})

def detalle_destino(request, destino_id):
    destino = get_object_or_404(Destino, id=destino_id)
    paquetes = Paquete.objects.filter(destino=destino)
    return render(request, 'sitio/detalle_destino.html', {
        'destino': destino,
        'paquetes': paquetes
    })
