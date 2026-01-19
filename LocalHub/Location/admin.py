from django.contrib import admin
from Location.models import Location

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")