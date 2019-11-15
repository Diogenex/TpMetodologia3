from django.shortcuts import get_object_or_404,render
from .models import Propiedad
from .models import Ciudad
from .models import Fecha_Alquiler

def index(request):
    lista_ciudades = Ciudad.objects.all()
    context = { 'lista_ciudades': lista_ciudades, }
    return render(request, 'reservas/home.html', context)

def propiedades(request):
    lista_propiedades = Propiedad.objects.all()
    context = { 'lista_propiedades': lista_propiedades, }
    return render(request, 'reservas/propiedades.html', context)

def propiedadesFiltradas(request):

    fechaDesde = request.POST.get('from_date')
    fechaHasta = request.POST.get('to_date')

    def square(x):
        return x.propiedad

    if fechaDesde and fechaHasta:
        
        diasReservacion = Fecha_Alquiler.objects.filter(
            fecha_alq__range=(fechaDesde, fechaHasta),
            reserva__isnull=True
        ).all()

        lista_propiedades = list(set(map(square, diasReservacion)))
    else:

        lista_propiedades = Propiedad.objects.all()


    context = { 'lista_propiedades': lista_propiedades, }
    return render(request, 'reservas/propiedades.html', context)

def propiedad(request, propiedad_id):
    diasReservacion = Fecha_Alquiler.objects.filter(propiedad= propiedad_id, reserva__isnull=True).all()
    propiedad = get_object_or_404(Propiedad, pk=propiedad_id)
    context = { 'propiedad': propiedad,
                'diasReservacion': diasReservacion,}
    return render(request, 'reservas/propiedad.html', context)

def reserva(request):
    return render(request, 'reservas/reserva.html')