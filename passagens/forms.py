from django import forms
from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *

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


    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_retorno = self.cleaned_data.get('data_retorno')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}

        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_ida_maior_que_data_retorno(data_ida, data_retorno, lista_de_erros)
        data_ida_maior_que_hoje(data_ida, data_pesquisa, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data
