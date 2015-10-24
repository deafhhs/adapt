from django.apps import AppConfig


class ClientsAppConfig(AppConfig):
    name = 'clients'
    verbose_name = 'ADAPT Client Management'


default_app_config = 'clients.ClientsAppConfig'
