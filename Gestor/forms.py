from django import forms
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from datetime import date
from .models import User

class MovementForm(forms.Form):
    name = forms.CharField(
        label="*Nombre",
        max_length=75, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r"^[A-Za-z\s]+$",
                message="El nombre solo puede contener letras y espacios."
            )
        ]
    )
    date = forms.DateField(
        label="*Fecha", 
        required=True,
        widget=forms.DateTimeInput(
            attrs={'type':'date', 'class': 'form-control'}
        ),
        validators=[
            MaxValueValidator(
                limit_value=date.today(),
                message="La fecha no puede ser posterior a hoy."
            )
        ]
    )
    type_movement = forms.ChoiceField(
        label="*Tipo",
        required=True,
        choices=[(True, "Ingreso"), (False, "Egreso")],
        widget=forms.Select(attrs={'id':'type','class':'form-select'})
    )
    amount = forms.FloatField(
        label="*Monto",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        validators=[
            MinValueValidator(
                limit_value=0.0,
                message=("Se debe ingresar el número en valores positivos.")
            )
        ]
    )
    category_input = forms.TypedChoiceField(
        label="*Categoría",
        required=True,
        choices=[],
        widget=forms.Select(attrs={'class':'form-select'}),
        coerce=int
    )
    category_output = forms.TypedChoiceField(
        label="*Categoría",
        required=True,
        choices=[],
        widget=forms.Select(attrs={'class':'form-select'}),
        coerce=int
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .utils import get_categories  # <-- lo traés adentro para evitar errores al migrar
        self.fields["category_input"].choices = get_categories(True)
        self.fields["category_output"].choices = get_categories(False)


class MovementFilter(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=False,
        max_length=75,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    min_date = forms.DateField(
        label="Desde",
        required=False,
        widget=forms.DateTimeInput(
            attrs={'type':'date', 'class': 'form-control'}
        )
    )
    max_date = forms.DateField(
        label="Hasta",
        required=False,
        widget=forms.DateTimeInput(
            attrs={'type':'date', 'class': 'form-control'}
        )
    )
    type_movement = forms.ChoiceField(
        label="Tipo",
        required=False,
        choices=[("1", "Ambos"), ("2", "Ingreso"), ("3", "Egreso")],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    amount = forms.FloatField(
        label="Monto",
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    order = forms.ChoiceField(
        label="Orden",
        required=False,
        initial="1",
        choices=[("1", "Reciente"), ("2", "Antiguo"), ("3", "A - Z"), ("4", "Z - A")],
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(
        label="*Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="*Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Repetir Contraseña",
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ["email", "password"]
    

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )