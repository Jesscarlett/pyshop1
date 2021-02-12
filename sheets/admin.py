from django.contrib import admin
from .models import Sheet
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class SheetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'file_url')


class SheetAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category', 'file_url')


admin.site.register(Sheet, SheetAdmin)


class SheetResource(resources.ModelResource):
    class Meta:
        model = Sheet




