from django.apps import AppConfig


class SgicrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.sgicr'
    def ready(self):
        import app.sgicr.signals
