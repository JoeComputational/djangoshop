from django.apps import AppConfig

#This is the shops configuration and where database models are stored
class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'