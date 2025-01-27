from django.urls import path
from Gestor.views import indexView, createMovement, deleteMovement, editMovement

urlpatterns = [
    path('', indexView, name="index"),
    path("new", createMovement, name="create"),
    path("delete/<int:id>", deleteMovement, name="delete"),
    path("edit/<int:id>", editMovement, name="edit")
]
