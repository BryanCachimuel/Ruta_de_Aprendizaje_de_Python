from django.contrib import admin

# Modelo
from .models import Post

# Register your models here.
#admin.site.register(Post)

# con este decorador se va a importar directamente al administrador
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'description', 'created')
    list_display_links = ('id', 'title',)
    list_filter = ('created', 'updated')
    search_fields = ('title', 'description')

    # para campos de solo lectura
    readonly_fields = ('created', 'updated')
