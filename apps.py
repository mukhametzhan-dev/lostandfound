from django.apps import AppConfig


class LostandfoundConfig(AppConfig):
    
    name = 'lostandfound'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import lostandfound.signals
