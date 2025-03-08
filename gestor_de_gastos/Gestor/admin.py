from django.contrib import admin
from .models import Movements, Categories

# Register your models here.
class MovementsAdmin(admin.ModelAdmin):
    fields = ["name", "date", "amount", "type_movement", "category"]
    list_display = ["name", "date", "amount", "type_movement", "category"]


admin.site.register(Movements, MovementsAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    fields = ["name", "class_name", "type_movement"]
    list_display = ["name", "class_name", "type_movement"]


admin.site.register(Categories, CategoriesAdmin)