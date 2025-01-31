from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import MovementForm
from .models import Movements


PAGES = 15


def index_view(request):
    """Muestra la pagina principal."""
    inputs = Movements.objects.filter(type_movement=True).order_by("date")
    outputs = Movements.objects.filter(type_movement=False).order_by("date")
    total = 0
    for obj in inputs:
        total += obj.amount
    
    for obj in outputs:
        total -= obj.amount

    return render(
        request, 
        "index.html", 
        {"inputs":inputs, "outputs":outputs, "total":total}
    )


def create_movement(request):
    """Muestra el formulario de movimientos y guarda los nuevos movimientos"""
    if request.method == "POST":
        form = MovementForm(request.POST)
        if form.is_valid():
            movement = Movements(
                name=request.POST.get('name'),
                date=request.POST.get('date'),
                amount=request.POST.get('amount'),
                type_movement=request.POST.get('type_movement')
            )
            movement.save()

            return redirect("index")
            
    else:
        form = MovementForm()
    
    return render(request, "create.html", {"form":form})


def delete_movement(request, id):
    """
        Recibe un id, si es valido elimina el objeto correspondiente,
        si no carga el template.
    """
    movement = Movements.objects.get(id=id)
    print(movement.type_movement)
    print(type(movement.type_movement))
    if request.method == 'POST':
        movement.delete()
        return redirect("index")
    
    return render(request, "delete.html", {"movement":movement})


def edit_movement(request, id):
    """Muestra el formulario de movimientos y guarda los nuevos movimientos"""
    movement = Movements.objects.get(id=id)
    if movement is None:
        return redirect("index")
    
    if request.method == "POST":
        form = MovementForm(request.POST)
        if form.is_valid():
            movement.name=form.cleaned_data['name']
            movement.date=form.cleaned_data['date']
            movement.amount=form.cleaned_data['amount']
            movement.type_movement=form.cleaned_data['type_movement']

            movement.save()

            return redirect("index")
            
    else:
        form = MovementForm(initial=movement.get_data())
    
    return render(request, "edit.html", {"form":form})


def list_movements(request, page=1):
    movements = Movements.objects.all()

    paginator = Paginator(movements, PAGES)
    movements = paginator.get_page(page)

    return render(request, "listMovements.html", {"movements":movements})