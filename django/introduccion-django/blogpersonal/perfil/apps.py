from django.apps import AppConfig


class PerfilConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil'
    # se puede traducir también la pestaña del administrador que redirige hacia los post
    #verbose_name = 'Perfiles'
