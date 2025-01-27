from django.contrib import admin
from .models import Movements

# Register your models here.
class MovementsAdmin(admin.ModelAdmin):
    fields = ["name", "date", "amount", "type_movement"]
    list_display = ["name", "date", "amount", "type_movement"]

admin.site.register(Movements, MovementsAdmin)