import json

'''
Nessa atividade, vamos usar dados do campeonato brasileiro 2018
(brasileirão) para estudar como acessar listas, dicionários,
e estruturas encadeadas (listas dentro de dicionários dentro de listas).
Os dados estão fornecidos em um arquivo (ano2018.json) que você 
pode abrir no Firefox, para tentar entender melhor.
Para rodar isso daqui, o arquivo de teste brasileirao_teste.py que
acompanha deve ser executado. É ele que vai testar as funções desenvolvidas
abaixo e dizer se parece estar tudo ok ou não. Há 20 testes lá, cada um deles
vale 0,5 pontos na nota do AC.
Se quiser ver os dados dentro do python, pode chamar a função
pega_dados que está no brasileirao_teste.py.
O que deve ser entregue é apenas este arquivo, com todas as modificações
necessárias para o sucesso dos exercícios. Os arquivos ano2018.json e
brasileirao_teste.py não devem ser alterados e nem entregues.
'''


'''
Primeiramente, altere esta função para que a mesma retorne o seu nome.
'''

def nome_do_aluno():
    return 'Pedro Fernandes Klein'


'''
********** EXERCÍCIO 1: **********
Crie uma função datas_de_jogo, que procura nos dados do brasileirão
e devolve uma lista de todas as datas em que houve jogo.
As datas devem ter o mesmo formato que tinham nos dados do brasileirão.
dica: busque em dados['fases']
Observe que essa função (e todas as demais!) recebem os dados dos
jogos numa variável dados. Essa variável contém todas as informações do
arquivo JSON que acompanha essa atividade.
''' 

def datas_de_jogo(dados):
    datas = dados['fases']['2700']['jogos']['data']
    #
    return datas
    raise Exception('Implemente isto!')


'''
********** EXERCÍCIO 2: **********
Crie uma função data_de_um_jogo, que recebe a id numérica de um jogo
e devolve a data em que ele ocorreu.
Se essa não for uma id válida, você deve devolver a string 'nao encontrado'.
Cuidado! Se você devolver uma string ligeiramente diferente, o teste
vai falhar.
Você provavelmente vai querer testar sua função no braço e não
somente fazer os meus testes. Para isso, note que muitos números
nesse arquivo estão representados não como números, mas sim como strings.
'''

def data_de_um_jogo(dados, id_jogo):
    try:
        data = dados['fases']['2700']['jogos']['id'][id_jogo]['data']
        return data
    except KeyError:
        return('nao encontrado')


'''
********** EXERCÍCIO 3: **********
Nos nossos dados, cada time tem um id e uma identificação numérica.
(você pode consultar as identificações numéricas em dados['equipes']).
Essas id também aparecem nos jogos. (onde? dê uma procurada!)
Desenvolva a próxima função que recebe a id numérica de um jogo, e devolve as
ids numéricas dos dois times envolvidos.
Vou deixar um código para você lembrar como retornar duas ids em um único return.
def ids_dos_times_de_um_jogo(dados, id_jogo):
    time1 = 12
    time2 = 13
    return time1, time2 # Assim a gente retorna as duas respostas em um único return.
'''

def ids_dos_times_de_um_jogo(dados, id_jogo):
    try:
        jogo = dados['fases']['2700']['jogos']['id'][id_jogo]
        time1 = jogo['time1']
        time2 = jogo['time2']
        return time1, time2
    except KeyError:
        print('nao encontrado')
# Assim nós retornamos as duas respostas em um único return.


'''
********** EXERCÍCIO 4: **********
Desenvolva a função que recebe a id_numerica de um time e retorna seu 'nome-comum'.
'''

def nome_time(dados, id_time):
    try:
        time = dados['equipes'][id_time]
        nome = time['nome-comum']
        return nome
    except KeyError:
        return('nao encontrado')


'''
********** EXERCÍCIO 5: **********
Desenvolva a função que "cruza" as duas anteriores. Recebe uma id de um jogo
e retorna os "nome-comum" dos dois times.
'''

def nomes_dois_times_em_um_jogo(dados, id_jogo):
    try:
        jogo = dados['fases']['2700']['jogos']['id'][id_jogo]
        time1 = jogo['time1']
        time2 = jogo['time2']
        
        nome1 = dados['equipes'][time1]['nome-comum']
        nome2 = dados['equipes'][time2]['nome-comum']
        return nome1, nome2
    except KeyError:
        return('nao encontrado')


'''
********** EXERCÍCIO 6: **********
Desenvolva a função que faça a busca "ao contrário".
Conhecendo o nome-comum de um time, queremos saber sua id.
Se o nome comum não existir, retorne 'nao encontrado'.
'''

def id_do_time(dados, nome_time):
    try:
        times = dados['equipes']
        for t in times:
            if times[t]['nome-comum'] == nome_time:
                return times[t]['id']
    except KeyError:
        print(times[t]['nome-comum'])
        return('nao encontrado')
        

'''
********** EXERCÍCIO 7: **********
Agora, desenvolva a função que faça uma busca "fuzzy".
Queremos procurar por 'Fla' e achar o Flamengo. Ou por 'Paulo' e achar o São Paulo.
Nessa busca, você recebe um nome, e verifica os campos 'nome-comum', 'nome-slug',
'sigla' e 'nome', tomando o cuidado de aceitar times se a string buscada aparece
dentro do nome (A string "Paulo" aparece dentro de "São Paulo").
Sua resposta deve ser uma lista de ids de times que "batem" com a pesquisa
(e pode ser vazia, se não achar ninguém).
'''

def busca_fuzzy(dados, nome_time):
    raise Exception('Implemente isto!')


'''
********** EXERCÍCIO 8: **********
Desenvolva a função que recebe a id de um time e retorne as ids de todos
os jogos em que esse time participou.
'''

def ids_dos_jogos_do_time(dados, time_id):
    raise Exception('Implemente isto!')


'''
********** EXERCÍCIO 9: **********
Usando as ids dos jogos em que um time participou, desenvolva a função que
descobre em que dias ele jogou.
Note que essa função recebe o nome-comum do time, não sua id.
Ela retorna uma lista das datas em que o time jogou.
'''

def datas_dos_jogos_do_time(dados, nome_time):
    raise Exception('Implemente isto!')


'''
********** EXERCÍCIO 10: **********
Desenvolva a função que recebe apenas o dicionário dos dados do brasileirão
e devolve um dicionário com quantos gols cada time fez.
'''

def dicionario_qtd_gols(dados):
    raise Exception('Implemente isto!')


'''
********** EXERCÍCIO 11: **********
Desenvolva a função que recebe apenas o dicionário dos dados do brasileirão
e devolve a id do time que fez mais gols no campeonato.
'''

def time_artilheiro(dados):
    raise Exception('Implemente isto!')


'''
********** EXERCÍCIO 12: **********
Desenvolva a função que recebe apenas o dicionário dos dados do brasileirão
e devolve um dicionário que conta, para cada estádio, quantas vezes ocorreu um jogo nele.
Ou seja, as chaves são ids de estádios e os valores são o número
de vezes que um jogo ocorreu no estádio.
'''

def idestadio_nrojogos(dados):
    raise Exception('Implemente isto!')


'''
********** EXERCÍCIO 13: **********
Desenvolva a função que recebe apenas o dicionário dos dados do brasileirão
e devolve o número  de times que o brasileirão qualifica para a libertadores.
Note que esse número está nos dados do parâmetro. Você deve pegar o número
a partir dos dados. Não basta retornar o valor correto, tem que acessar os dados
fornecidos.
Consulte a parte de faixas de times no dicionário.
'''

def qualificados_liberta(dados):
    raise Exception('Implemente isto!')


'''
********** EXERCÍCIO 14: **********
Desenvolva a função que recebe um tamanho e retorna uma lista
com len(lista) == tamanho, com as ids dos times melhor classificados.
Por exemplo, ids_dos_melhor_classificados(dados, 6) tem que trazer as ids
dos 6 times melhor classificados.
'''

def ids_melhores_classificados(dados, numero):
    raise Exception('Implemente isto!')


'''
********** EXERCÍCIO 15: **********
Usando as duas funções anteriores, deselvolva uma outra função que retorne uma
lista de todos os times classificados para a libertadores em virtude do
campeonato brasileiro.
Lembre-se de consultar a estrutura, tanto para obter a classificação, quanto
para obter o número correto de times a retornar.
'''

def classificados_liberta(dados):
    raise Exception('Implemente isto!')


'''
********** EXERCÍCIO 16: **********
Da mesma forma que podemos obter a informação dos times classificados
para a libertadores, também podemos obter os times na zona de rebaixamento.
Desenvolva a função que recebe apenas o dicionário de dados do brasileirão,
e retorna uma lista com as ids dos times rebaixados.
Consulte a zona de rebaixamento do dicionário de dados, não deixe
os valores "chumbados" na função.
'''

def rebaixados(dados):
    raise Exception('Implemente isto!')


'''
********** EXERCÍCIO 17: **********
Desenvolva uma função que recebe, além do dicionário de dados do brasileirão, uma id de time.
Ela retorna a classificação desse time no campeonato.
Por exemplo, classificacao_do_time_por_id(dados, '695') devolve 14 porque o time com a id 695
é a Chapecoense, que terminou o campeonato na décima-quarta posição.
Se a id não for válida, retorna a string 'nao encontrado'.
'''

def classificacao__por_id(dados, time_id):
    raise Exception('Implemente isto!')