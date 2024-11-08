from django.contrib import admin

from applica.models import Conductor, Vehiculo, Marca, Modelo, ConductorVehiculo, RevisionTecnica, Infraccion, \
    Incidencia, ExcesoVelocidad

from unfold.admin import ModelAdmin

from applica.sites import custom_admin_site


@admin.register(Conductor, site=custom_admin_site)
class ConductorAdmin(ModelAdmin):
    list_display = ("id", "nombre", "licencia_conducir", "dni", "direccion",)
    search_fields = ("id", "nombre", "licencia_conducir", "dni", "direccion")


@admin.register(Vehiculo, site=custom_admin_site)
class VehiculoAdmin(ModelAdmin):
    list_display = ("id", "placa", "marca", "modelo",)
    search_fields = ("id", "placa", "marca__nombre", "modelo__nombre")
    autocomplete_fields = ("modelo", "marca")


@admin.register(Marca, site=custom_admin_site)
class MarcaAdmin(ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")


@admin.register(Modelo, site=custom_admin_site)
class ModeloAdmin(ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")


@admin.register(ConductorVehiculo, site=custom_admin_site)
class ConductorVehiculoAdmin(ModelAdmin):
    list_display = ("id", "conductor", "vehiculo", "fecha_asignacion", "esta_activo")
    search_fields = ("id", "conductor__dni", "conductor__nombre", "conductor__licencia_conducir", "vehiculo__placa")


@admin.register(RevisionTecnica, site=custom_admin_site)
class RevisionTecnicaAdmin(ModelAdmin):
    list_display = ("id", "vehiculo", "fecha_revision", "resultado", "observaciones")
    search_fields = ('id', "vehiculo__placa",)


@admin.register(Infraccion, site=custom_admin_site)
class InfraccionAdmin(ModelAdmin):
    list_display = ("id", "conductor", "fecha_infraccion", "fecha_infraccion", "monto", "pagada")
    search_fields = ("id", "conductor__dni", "conductor__nombre")


@admin.register(Incidencia, site=custom_admin_site)
class IncidenciaAdmin(ModelAdmin):
    list_display = ("id", "conductor", "fecha_incidencia", "descripcion", "tipo")
    search_fields = ("id", "conductor__dni", "conductor__nombre")
    autocomplete_fields = ('conductor',)


@admin.register(ExcesoVelocidad, site=custom_admin_site)
class ExcesoVelocidadAdmin(ModelAdmin):
    list_display = ("id", "vehiculo", "fecha_evento", "velocidad", "ubicacion")
    search_fields = ("id", "vehiculo__placa")
    autocomplete_fields = ('vehiculo',)
