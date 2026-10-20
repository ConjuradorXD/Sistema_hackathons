from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'nome_item', 'tipo_item', 'peso', 'raridade', 'descricao_item',
            'nome_encontrador', 'graduacao', 'local_encontrado', 'data_encontrado',
        ]
        widgets = {
            'nome_item': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome_item'}),
            'tipo_item': forms.TextInput(attrs={'class': 'form-control', 'id': 'tipo_item'}),
            'peso': forms.TextInput(attrs={'class': 'form-control', 'id': 'peso'}),
            'raridade': forms.TextInput(attrs={'class': 'form-control', 'id': 'raridade'}),
            'descricao_item': forms.Textarea(attrs={'class': 'form-control', 'id': 'descricao_item', 'rows': 3}),
            'nome_encontrador': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome_encontrador'}),
            'graduacao': forms.TextInput(attrs={'class': 'form-control', 'id': 'graduacao'}),
            'local_encontrado': forms.TextInput(attrs={'class': 'form-control', 'id': 'local_encontrado'}),
            'data_encontrado': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date', 'class': 'form-control', 'id': 'data_encontrado'},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.required = True
        self.fields['descricao_item'].required = False
