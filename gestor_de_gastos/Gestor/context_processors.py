from .utils import is_authenticated


def global_context(request):
    return {"is_authenticated": is_authenticated(request)}