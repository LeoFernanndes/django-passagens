from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100, required=True)
    destino = forms.CharField(label='Destino', max_length=100, required=True)
    data_ida = forms.DateField(label='Ida', required=True, widget=DatePicker())
    data_retorno = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label="Classe", choices=tipos_de_classe)
    informacoes = forms.CharField(
        label="Informações adicinais",
        max_length=200,
        widget=forms.Textarea,
        required=False
    )
    email = forms.CharField(max_length=100)

    def clean_origem(self):
        origem = self.cleaned_data.get('origem')
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError("Não incluir valores numéricos no campo origem")
        else:
            return origem