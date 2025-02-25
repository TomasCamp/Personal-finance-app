from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User  # Importa el modelo personalizado

class CustomUserBackend(BaseBackend):
    """Backend para autenticar usuarios normales con email y password."""

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):  # Verifica la contraseña
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None