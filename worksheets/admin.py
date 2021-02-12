from django.contrib import admin
from .models import WorkSheet


# Register your models here.

class WorkSheetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'file_url', 'file')


admin.site.register(WorkSheet, WorkSheetAdmin)

