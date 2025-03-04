from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    # se puede traducir también la pestaña del administrador que redirige hacia los post
    #verbose_name = 'Blogs'
