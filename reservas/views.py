from django.shortcuts import get_object_or_404,render
from .models import Propiedad
from .models import Ciudad
from .models import Fecha_Alquiler
from .models import Reserva
import datetime
from django.utils.crypto import get_random_string

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
    ciudad = request.POST.get('city')
    cantidad = request.POST.get('pax_qty')

    lista_opciones = []
    lista_info = {}
    lista_info ['desde'] = fechaDesde
    lista_info ['hasta'] = fechaHasta
    lista_info ['ciudad'] = ciudad
    lista_info ['cantidad'] = cantidad
    lista_opciones.append(lista_info)    

    def square(x):
        return x.propiedad

    if fechaDesde and fechaHasta:
        
        diasReservacion = Fecha_Alquiler.objects.filter(
            fecha_alq__range=(fechaDesde, fechaHasta),
            reserva__isnull=True,
        ).all()

       
        lista_propiedades = list(set(map(square, diasReservacion)))
        
    else:

        lista_propiedades = Propiedad.objects.all()


    context = { 'lista_propiedades': lista_propiedades,
                'lista_opciones' : lista_opciones }
    return render(request, 'reservas/propiedades.html', context)

def propiedad(request, propiedad_id):
    diasReservacion = Fecha_Alquiler.objects.filter(propiedad= propiedad_id, reserva__isnull=True).all()
    propiedad = get_object_or_404(Propiedad, pk=propiedad_id)
    context = { 'propiedad': propiedad,
                'diasReservacion': diasReservacion,}
    return render(request, 'reservas/propiedad.html', context)

def reserva(request, propiedad_id):
    diasReservacion = Fecha_Alquiler.objects.filter(propiedad=propiedad_id, id__in=request.POST.getlist('reservation_dates')).all()
    reserva = Reserva()

    
    propiedad = Propiedad.objects.get(id=propiedad_id)
    
    reserva.fecha_reserva = datetime.date.today()
    reserva.propiedad = propiedad
    reserva.codigo = get_random_string(length=12)
    
    reserva.total = len(request.POST.getlist('reservation_dates')) * propiedad.precio_diario
    reserva.save()


    reservaId = Reserva.objects.latest('id')

    
    diasReservacion.update(reserva=reservaId)

    return render(request, 'reservas/reserva.html', {
        'propiedad': propiedad,
        'reserva': reserva,
        'diasReservacion': diasReservacion
    })
   