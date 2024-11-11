from django.contrib import admin
from django.urls import path
from unfold.sites import UnfoldAdminSite

from applica.views import DashboardTemplateView


class CustomAdminSite(UnfoldAdminSite):
    site_header = "Dorado App"
    site_title = "Dorado APP"
    index_title = "Bienvenido Admin Dorado"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('mi-vista/', self.admin_view(DashboardTemplateView.as_view()), name='dashboard'),
        ]
        return custom_urls + urls


custom_admin_site = CustomAdminSite(name="custom_admin_site")
