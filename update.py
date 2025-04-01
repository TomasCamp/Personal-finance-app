import os
import django

# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestor_de_gastos.settings")  # Reemplaza 'tu_proyecto' con el nombre de tu proyecto
django.setup()

from Gestor.models import Categories

def update_class_name():
    # Modificar una categoría específica
    category = Categories.objects.get(id=1)
    category.class_name = "check_box_outline_blank"
    category.save()
    print(f"Categoría {category.id} actualizada con class_name: {category.class_name}")

    category = Categories.objects.get(id=2)
    category.class_name = "check_box_outline_blank"
    category.save()
    print(f"Categoría {category.id} actualizada con class_name: {category.class_name}")

    category = Categories.objects.get(id=3)
    category.class_name = "work"
    category.save()
    print(f"Categoría {category.id} actualizada con class_name: {category.class_name}")

    category = Categories.objects.get(id=4)
    category.class_name = "bar_chart_4_bars"
    category.save()
    print(f"Categoría {category.id} actualizada con class_name: {category.class_name}")

    category = Categories.objects.get(id=5)
    category.class_name = "draft"
    category.save()
    print(f"Categoría {category.id} actualizada con class_name: {category.class_name}")

    category = Categories.objects.get(id=6)
    category.class_name = "shopping_cart"
    category.save()
    print(f"Categoría {category.id} actualizada con class_name: {category.class_name}")

    category = Categories.objects.get(id=7)
    category.class_name = "directions_car"
    category.save()
    print(f"Categoría {category.id} actualizada con class_name: {category.class_name}")

    category = Categories.objects.get(id=8)
    category.class_name = "health_and_safety"
    category.save()
    print(f"Categoría {category.id} actualizada con class_name: {category.class_name}")

    category = Categories.objects.get(id=9)
    category.class_name = "local_mall"
    category.save()
    print(f"Categoría {category.id} actualizada con class_name: {category.class_name}")

if __name__ == "__main__":
    update_class_name()