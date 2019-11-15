from django.contrib import admin
from .models import Ciudad , Reserva, Fecha_Alquiler, Propiedad
# Register your models here.from django.contrib import admin



admin.site.register(Ciudad)
admin.site.register(Reserva)

class FechaAlquiler_Inline(admin.TabularInline):
    model = Fecha_Alquiler
    fk_name = 'propiedad'
    max_num = 7
    fields = ['fecha_alq']


""" class PropiedadAdmin(admin.ModelAdmin):
    fields = ['ciudad','imagen','titulo', 'descripcion', 'precio_diario', 'max_pax']
    inlines = [FechaAlquiler_Inline]

    def save_model(self, request, obj, form, change):
        obj.dueño = request.user
        return super(PropiedadAdmin, self).save_model(request, obj, form, change)

admin.site.register(Propiedad, PropiedadAdmin) """

class AdminBuilding(admin.ModelAdmin):
    inlines = [FechaAlquiler_Inline]


admin.site.register(Propiedad, AdminBuilding)
