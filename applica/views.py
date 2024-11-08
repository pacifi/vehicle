from tempfile import template

from django.shortcuts import render


def dashboard(request):
    template = 'vehicle/dashboard.html'
    return render(request, template)


def reporte_velocidad(request):
    template = 'vehicle/reporte_velocidad.html'
    return render(request, template)
