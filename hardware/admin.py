from django.contrib import admin

from hardware.models import Hardware


@admin.register(Hardware)
class HardwareAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'serial_number')
