from django.apps import AppConfig


class SiteAcademiaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_academia'


class SiteAcademiaConfig(AppConfig):
    name = 'site_academia'

    def ready(self):
        import site_academia.signals
