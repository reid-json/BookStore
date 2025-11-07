# AA_ObserverPattern_Notify/apps.py
from django.apps import AppConfig


class AAObserverPatternNotifyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AA_ObserverPattern_Notify'

    def ready(self):
        import AA_ObserverPattern_Notify.signals