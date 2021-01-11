from django.contrib import admin
from .models import DataSchema, DataSet, Field

@admin.register(DataSchema)
class DataSchemaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated',)

@admin.register(DataSet)
class DataSetAdmin(admin.ModelAdmin):
    list_display = ('file', 'schema', 'created', 'status', )

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('type', 'order', 'schema', )