from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'fins_dashboard'
    verbose_name = "Fins Dashboard"
