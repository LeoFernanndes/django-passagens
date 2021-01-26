def origem_destino_iguais(origem, destino, lista_de_erros):
    """
    Verifica se origem e destino são iguais.
    Estritamnte iguais. Ainda falta incluir métodos de regex para verificar
    nomed diferentes que queiram dizer a mesma coisa
    """
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais' 

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """
    Verifica se o campo apresenta números
    """
    if any(char.isdigit for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números nesse campo'


def data_ida_maior_que_data_retorno(data_ida, data_retorno, lista_de_erros):
    """
    Verifica se a data de retorno é de fato mais distante que a data de ida
    """
    if data_ida > data_retorno:
        lista_de_erros['data_retorno'] = 'Data de retorno deve ser mais distate que a de ida'

def data_ida_maior_que_hoje(data_ida, data_pesquisa, lista_de_erros):
    """Verifica se a ida é futura"""
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida deve ser de hoje pra frente'