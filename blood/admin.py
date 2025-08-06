from django.contrib import admin
from .models import BloodStock, BloodRequest, Donor

admin.site.register(BloodStock)
admin.site.register(Donor)

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'units', 'status')
    fields = ('user', 'group', 'units', 'status')
