from django.db import models
from django.utils import timezone

# Create your models here.
class Movements(models.Model):
    name = models.CharField(max_length=75, null=False, verbose_name="Nombre")
    date = models.DateField(verbose_name="Fecha", default=timezone.now, null=False)
    amount = models.FloatField(verbose_name="Monto", null=False)
    # type_movement: True = input, false = output
    type_movement = models.BooleanField(verbose_name="Tipo de Movimiento", null=False, default=False)

    def get_data(self):
        return {
            "name": self.name,
            "date": self.date.isoformat(),
            "amount": self.amount,
            "type_movement": self.type_movement
        }