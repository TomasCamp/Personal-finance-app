from functools import wraps
from django.shortcuts import redirect
from .models import Categories

def is_authenticated(request):
    """Devuelve si el usuario está autenticado"""
    return request.user.is_authenticated

def login_check(view_func):
    """Decorador que redirige a login si el usuario no hizo login."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not is_authenticated(request):
            return redirect("login")
        return view_func(request, *args, **kwargs)
    return wrapper

def get_categories(movement):
    categories = Categories.objects.filter(type_movement=movement).all()
    values = []
    for category in categories:
        values.append((category.id, category.name))
    return values