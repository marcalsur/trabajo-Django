from django import forms

pizzas= [
    ('muzza', 'Muzzarela'),
    ('napo', 'Napolitana'),
    ('jamon', 'Jamon'),
    ('morron', 'Morron'),
    ('doble', 'Doble Muzzarela'),
    ]

class PedidoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    mail = forms.EmailField(label="Mail", required=True)
    direccion = forms.CharField(label="Direccion", required=True)
    pizza= forms.CharField(label='Seleccione su gusto', widget=forms.Select(choices=pizzas))
