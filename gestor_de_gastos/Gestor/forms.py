from django import forms

class MovementForm(forms.Form):
    name = forms.CharField(
        label="*Nombre",
        max_length=75, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    date = forms.DateField(
        label="*Fecha", 
        required=True,
        widget=forms.DateTimeInput(
            attrs={'type':'date', 'class': 'form-control'}
        )
    )
    type_movement = forms.ChoiceField(
        label="*Tipo",
        required=True,
        choices=[(True, "Ingreso"), (False, "Egreso")],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    amount = forms.FloatField(
        label="*Monto",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )