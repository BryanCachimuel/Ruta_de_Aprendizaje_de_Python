from django.contrib import admin

# Modelo
from .models import Project 

# Register your models here.
#admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created')
    list_editable = ('title', )
    list_filter = ('title', 'created', 'updated')
    search_fields = ('title',)

    # para campos de solo lectura
    readonly_fields = ('created', 'updated')