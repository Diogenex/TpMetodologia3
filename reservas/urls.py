from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('propiedades/', views.propiedades, name='propiedades'),
    path('filtradas/', views.propiedadesFiltradas, name='filtradas'),
    path('<int:propiedad_id>/', views.propiedad, name='propiedad'),
    path('<int:propiedad_id>/reserva/', views.reserva, name='reserva')
]
