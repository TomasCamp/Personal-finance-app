from django.urls import path
from Gestor.views import index_view, create_movement, delete_movement, edit_movement, list_movements

urlpatterns = [
    path('', index_view, name="index"),
    path("new", create_movement, name="create"),
    path("delete/<int:id>", delete_movement, name="delete"),
    path("edit/<int:id>", edit_movement, name="edit"),
    path("list-movements/", list_movements, name="list_movements_default"),
    path("list-movements/<int:page>", list_movements, name="list_movements")
]
