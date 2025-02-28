from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("El usuario debe tener un email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.email
    

class Movements(models.Model):
    name = models.CharField(max_length=75, null=False, verbose_name="Nombre")
    date = models.DateField(verbose_name="Fecha", default=timezone.now, null=False)
    amount = models.FloatField(verbose_name="Monto", null=False)
    # type_movement: True = input, false = output
    type_movement = models.BooleanField(verbose_name="Tipo de Movimiento", null=False, default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movements")

    def get_data(self):
        return {
            "name": self.name,
            "date": self.date.isoformat(),
            "amount": self.amount,
            "type_movement": self.type_movement
        }
