from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from .forms import MovementForm, MovementFilter, SignUpForm, LoginForm
from .models import Movements, User
from .utils import login_check


PAGES = 15


@login_check
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


@login_check
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


@login_check
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


@login_check
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


@login_check
def list_movements(request, page=1):
    """Genera un listado de movimientos y los filtra."""
    form = MovementFilter(request.GET)
    movements = Movements.objects
    if form.is_valid():
        print("Entró")
        name = form.cleaned_data.get('name')
        if name:
            movements = movements.filter(name__icontains=name)

        min_date = form.cleaned_data.get('min_date')
        if min_date:
            movements = movements.filter(date__gte=min_date)
        max_date = form.cleaned_data.get('max_date')
        if max_date:
            movements = movements.filter(date__lte=max_date)
        
        type_movement = form.cleaned_data.get('type_movement')
        if type_movement == "2":
            movements = movements.filter(type_movement=True)
        elif type_movement == "3":
            movements = movements.filter(type_movement=False)

        amount = form.cleaned_data.get('amount')
        if amount:
            movements = movements.filter(amount=amount)
        
        order = form.cleaned_data.get('order') or "1"
        if order == "1":
            movements = movements.order_by("-date")
        elif order == "2":
            movements = movements.order_by("date")
        elif order == "3":
            movements = movements.order_by("name")
        elif order == "4":
            movements = movements.order_by("-name")

    paginator = Paginator(movements.all(), PAGES)
    movements = paginator.get_page(page)

    return render(
        request, 
        "listMovements.html", 
        {"movements":movements, "form":form}
    )


def sign_up(request):
    """Muestra la pagina para crear usuarios y los crea."""
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUpForm()
    
    return render(request, "sign_up.html", {"form":form})


def login_view(request):
    """Permite iniciar sesión."""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect("index")
            else:
                form.add_error(None, "Credenciales incorrectas")
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form":form})


@login_check
def logout_view(request):
    logout(request)
    return redirect("login")